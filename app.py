import psycopg2
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from intent_detection import detect_intent
from response_generator import generate_response
from database import get_connection
from functools import wraps
from flask_login import login_required


app = Flask(__name__)
app.secret_key = 'bjb123'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def db_conn():
    conn = psycopg2.connect(
        database="api_bjb",
        host="localhost",
        user="postgres",
        password="marcell",
        port="5432",
    )
    return conn

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

@app.route('/admin')
@login_required
def admin():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_specification ORDER BY id ASC")
    api_specification = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('admin.html', api_specification=api_specification)

@app.route('/create', methods=['POST'])
def create():
    conn = get_connection()
    cur = conn.cursor()
    keyword = request.form['keyword']
    response = request.form['response']
    
    cur.execute('''INSERT INTO api_specification (keyword, response) VALUES (%s, %s)''', (keyword, response))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/update', methods=['POST'])
def update():
    conn = db_conn()
    cur = conn.cursor()

    keyword = request.form['keyword']
    response = request.form['response']
    id = request.form['id']

    cur.execute(
        '''UPDATE api_specification SET keyword = %s, response = %s WHERE id = %s''', (keyword, response, id))
    
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for('admin'))

@app.route('/delete', methods=['POST'])
def delete():
    conn = db_conn()
    cur = conn.cursor()
    
    id = request.form['id']

    cur.execute('''DELETE FROM api_specification WHERE id = %s''', (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for('admin'))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_query = request.json.get('query')
        intent = detect_intent(user_query)
        response = generate_response(intent)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
