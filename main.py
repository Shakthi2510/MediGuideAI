from flask import Flask, request, render_template, jsonify
import sqlite3
from fpdf import FPDF
from googletrans import Translator
from sklearn.tree import DecisionTreeClassifier
import schedule
import time
from datetime import datetime, timedelta

app = Flask(__name__)


medication_reminders = []


X = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  
y = ["Cold", "Flu", "Heart Attack"]
model = DecisionTreeClassifier()
model.fit(X, y)


health_tips = {
    "Cold": "Stay hydrated and rest.",
    "Flu": "Get plenty of rest and drink warm fluids.",
    "Heart Attack": "Maintain a healthy diet and exercise regularly."
}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/suggest', methods=['GET'])
def suggest():
    query = request.args.get('term', '').lower()
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT symptom FROM health_data WHERE symptom LIKE ?", (f"%{query}%",))
    results = cursor.fetchall()
    conn.close()
    suggestions = [row[0] for row in results]
    return jsonify(suggestions)


@app.route('/search', methods=['POST'])
def search():
    user_input = request.form['symptom'].lower()
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT symptom, solution, tablet, reason FROM health_data WHERE symptom LIKE ?", (f"%{user_input}%",))
    result = cursor.fetchone()
    conn.close()

    if not result:
        corrected_symptom = user_input.capitalize()
        solution = f"No solution found for '{corrected_symptom}'. Please consult a doctor."
        tablet = "No tablet recommended"
        reason = "No reason provided"
    else:
        corrected_symptom = result[0].capitalize()
        solution = result[1]
        tablet = result[2] if result[2] else "No tablet recommended"
        reason = result[3] if result[3] else "No reason provided"
    return render_template('result.html', symptom=corrected_symptom, solution=solution, tablet=tablet, reason=reason)


@app.route('/solution/<symptom>')
def show_solution(symptom):
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT symptom, solution, tablet, reason FROM health_data WHERE symptom LIKE ?", (f"%{symptom}%",))
    result = cursor.fetchone()
    conn.close()

    if result:
        solution, tablet, reason = result[1], result[2], result[3]
        return render_template('result.html', symptom=symptom, solution=solution, tablet=tablet, reason=reason)
    else:
        return "Solution not found", 404

@app.route('/add_reminder', methods=['POST'])
def add_reminder():
    data = request.json
    medication_reminders.append(data)
    return jsonify({"message": "Reminder added successfully!"}), 200

def check_reminders():
    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    for reminder in medication_reminders:
        if reminder['time'] == now:
            print(f"Reminder: Take your {reminder['medication_name']} - {reminder['dosage']}")


@app.route('/export_report', methods=['POST'])
def export_report():
    data = request.json
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for key, value in data.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    filename = "health_report.pdf"
    pdf.output(filename)
    return jsonify({"message": "Report exported successfully", "filename": filename}), 200

@app.route('/symptom_checker', methods=['POST'])
def symptom_checker():
    symptom = request.form['symptom'].lower()
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("SELECT symptom, solution, tablet, reason FROM health_data WHERE symptom LIKE ?", (f"%{symptom}%",))
    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({
            "symptom": result[0],
            "solution": result[1],
            "tablet": result[2] if result[2] else "No tablet recommended",
            "reason": result[3] if result[3] else "No reason provided"
        })
    else:
        return jsonify({"message": "Symptom not found. Please consult a doctor."}), 404


@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_language = request.form['language']
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return jsonify({"translated_text": translated.text})


@app.route('/predict_diagnosis', methods=['POST'])
def predict_diagnosis():
    user_symptoms = request.json['symptoms']
    prediction = model.predict([user_symptoms])
    return jsonify({"diagnosis": prediction[0]})

@app.route('/health_tips/<condition>', methods=['GET'])
def get_health_tips(condition):
    tip = health_tips.get(condition, "No tips available.")
    return jsonify({"health_tips": tip})


@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    user_feedback = request.form['feedback']
    conn = sqlite3.connect('health.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO feedback (feedback) VALUES (?)", (user_feedback,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Feedback submitted successfully!"})


if __name__ == '__main__':
    schedule.every(1).minute.do(check_reminders)
    app.run(debug=True)
