# MediGuideAI

MediGuideAI is a simple and intuitive health advisor web application. Users can input their symptoms, receive possible solutions, recommended medications, and associated reasons. This project demonstrates the integration of front-end, back-end, and database technologies to deliver a functional and user-friendly interface.

Features
Search for symptoms and view possible solutions.
Live symptom suggestions while typing.
Responsive design for mobile and desktop devices.
Utilizes SQLite for storing and retrieving health data.
Dynamic animations for a better user experience.
Demo
Include a screenshot or GIF of your project if available. You can add one like this:

markdown
Copy code
![Demo Screenshot](path/to/screenshot.png)
Prerequisites
Before running the project, ensure the following are installed on your system:

Python 3.10 or later
Flask (for the web server)
SQLite (for the database)
npm (optional, for managing additional front-end dependencies)
JQuery (linked in the project via CDN)
Getting Started
Follow these steps to set up the project on your local machine:

1. Clone the Repository
bash
Copy code
git clone https://github.com/your-username/MediGuideAI.git
cd MediGuideAI
2. Install Dependencies
Install Flask and its dependencies:

bash
Copy code
pip install flask
3. Set Up the Database
Ensure the SQLite database health_data.db exists in the project root. To initialize the database:

Create a file called health_data.sql containing:
sql
Copy code
CREATE TABLE health_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptom TEXT NOT NULL,
    solution TEXT NOT NULL,
    tablet TEXT NOT NULL,
    reason TEXT NOT NULL
);
Run the script to initialize the database:
bash
Copy code
sqlite3 health_data.db < health_data.sql
Populate the table with data:
bash
Copy code
sqlite3 health_data.db
INSERT INTO health_data (symptom, solution, tablet, reason) VALUES ('fever', 'Take rest and stay hydrated', 'Paracetamol', 'Reduces body temperature');
4. Run the Application
Start the Flask development server:

bash
Copy code
python main.py
The application will be accessible at http://127.0.0.1:5000/.

Usage
Open the application in your web browser.
Enter a symptom in the input field.
Select suggestions or press Find Solution to view solutions and recommendations.
Click Search Again to restart.
Project Structure
csharp
Copy code
MediGuideAI/
│
├── templates/         # HTML templates
│   ├── index.html     # Main search page
│   └── result.html    # Solution results page
│
├── static/            # Static files (CSS, JS)
│   └── styles.css     # Custom styles
│
├── health_data.db     # SQLite database
├── main.py            # Flask application logic
└── README.md          # Project documentation
Contributing
Contributions are welcome! If you'd like to improve the project:

Fork the repository.
Create a feature branch: git checkout -b feature-name.
Commit your changes: git commit -m "Add new feature".
Push to the branch: git push origin feature-name.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

