# MainCrafts Internship – Task 1

## User Management Web Application

A beginner-friendly full-stack web application built with Python, Flask, HTML, CSS and SQLite.

## Features

- Home page with a user input form
- Add user details through the web interface
- Store user records permanently in SQLite
- Fetch and display all users in a table
- Basic responsive CSS styling
- Duplicate-email validation
- Required-field validation

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- SQLite

## Project Structure

```text
maincrafts_task1/
├── app.py
├── database.db
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── screenshots/
```

## Project Flow

1. The user opens the Flask application in a browser.
2. Flask serves the HTML page from the `templates` folder.
3. The user enters name, email, phone and city.
4. The form sends the data to the Flask backend using a POST request.
5. Flask validates the fields and inserts the record into SQLite.
6. Flask retrieves all stored users and renders them in the table.
7. The SQLite database keeps the records after the application is closed.

## How to Run

### 1. Open a terminal in the project folder

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Flask

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

### 5. Open in a browser

```text
http://127.0.0.1:5000
```

## Submission Checklist

- [ ] Project folder / code files
- [ ] Screenshots of the running application
- [ ] `database.db`
- [ ] `README.md`
- [ ] GitHub repository link, if required by the internship submission instructions
