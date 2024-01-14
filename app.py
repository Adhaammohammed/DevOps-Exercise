from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

def create_connection():
    return psycopg2.connect(
        host='db',
        port=5432,
        user='admin',
        password='password',  # Corrected this line
        database='voting_app'
    )
   

def initialize_database():
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS votes (id SERIAL PRIMARY KEY, choice TEXT)')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form['choice']
    initialize_database()
    # Insert the vote into the database
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO votes (choice) VALUES (%s)', (choice,))
        conn.commit()

    return redirect(url_for('results'))

@app.route('/results')
def results():
    # Retrieve votes from the database
    with create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT choice, COUNT(id) FROM votes GROUP BY choice')
            result = cursor.fetchall()

    return render_template('results.html', result=result)

if __name__ == '__main__':
    initialize_database()
    app.run(debug=True)
