MediGuideAI


MediGuideAI is a simple and intuitive health advisor web application. Users can input their symptoms, receive possible solutions, recommended medications, and associated reasons. This project demonstrates the integration of front-end, back-end, and database technologies to deliver a functional and user-friendly interface.

Features


☻Search for symptoms and view possible solutions.

☻Live symptom suggestions while typing.

☻Responsive design for mobile and desktop devices.

☻Utilizes SQLite for storing and retrieving health data.

☻Dynamic animations for a better user experience.

Prerequisites

Before running the project, ensure the following are installed on your system:

1.Python 3.10 or later

2.Flask (for the web server)

3.SQLite (for the database)

4.npm (optional, for managing additional front-end dependencies)

5.JQuery (linked in the project via CDN)

Getting Started

Follow these steps to set up the project on your local machine:

1. Clone the Repository
   
        git clone https://github.com/your-username/MediGuideAI.git
        cd MediGuideAI
3. Install Dependencies
    
   Install Flask and its dependencies:

         
        pip install flask
5. Set Up the Database
  
   Ensure the SQLite database health_data.db exists in the project root. To initialize the database:

        Create a file called health_data.sql containing:
        sql
        CREATE TABLE health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symptom TEXT NOT NULL,
            solution TEXT NOT NULL,
            tablet TEXT NOT NULL,
            reason TEXT NOT NULL
        );

   
   Run the script to initialize the database:

           
            
           sqlite3 health_data.db < health_data.sql
           Populate the table with data:
           sqlite3 health_data.db
           INSERT INTO health_data (symptom, solution, tablet, reason) VALUES ('fever', 'Take rest and stay hydrated', 'Paracetamol', 'Reduces body temperature');

   
7. Run the Application
   
   Start the Flask development server:

         
        python main.py
        The application will be accessible at http://127.0.0.1:5000/.

Usage

1.Open the application in your web browser.

2.Enter a symptom in the input field.

3.Select suggestions or press Find Solution to view solutions and recommendations.

4.Click Search Again to restart.


Project Structure


    csharp
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

1.Fork the repository.

2.Create a feature branch: git checkout -b feature-name.

3.Commit your changes: git commit -m "Add new feature".

4.Push to the branch: git push origin feature-name.

5.Submit a pull request.

