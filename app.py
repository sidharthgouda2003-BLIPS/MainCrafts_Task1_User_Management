from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.config['SECRET_KEY'] = 'maincrafts-task1-secret-key'

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            city TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        phone = request.form.get('phone', '').strip()
        city = request.form.get('city', '').strip()

        if not all([name, email, phone, city]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('index'))

        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (name, email, phone, city) VALUES (?, ?, ?, ?)',
                (name, email, phone, city)
            )
            conn.commit()
            flash('User added successfully!', 'success')
        except sqlite3.IntegrityError:
            flash('A user with this email already exists.', 'error')
        finally:
            conn.close()

        return redirect(url_for('index'))

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
