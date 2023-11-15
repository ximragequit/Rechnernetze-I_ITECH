from flask import Flask, g, render_template, send_from_directory
import psycopg2
import os

app = Flask(__name__)

db_host = '10.1.0.6'
db_port = 5432
db_database = 'spaceone'
db_usr = 'admin_hs'
db_pw = 'Test+123456789'


conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_database,
    user=db_usr,
    password=db_pw
    )

# Hier füge eine Funktion hinzu, um die Daten aus der Datenbank abzurufen.
def get_data_from_db(table):
    cursor = conn.cursor()

    # Beispielabfrage, du solltest dies entsprechend deiner Datenbankstruktur anpassen.
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()

    cursor.close()
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/database')
def database():
    data = get_data_from_db('products')
    return render_template('database.html', data=data)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

