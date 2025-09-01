from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Initialize database and create table if not exists
def init_db():
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num1 REAL,
            num2 REAL,
            operation TEXT,
            result REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Save calculation to database
def save_calculation(num1, num2, operation, result):
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO history (num1, num2, operation, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (num1, num2, operation, result, timestamp))
    conn.commit()
    conn.close()

# Route to perform calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
    except:
        return jsonify({'error': 'Invalid input'}), 400

    # Perform calculation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    # Save to database
    save_calculation(num1, num2, operation, result)

    return jsonify({'result': result})

# Route to get calculation history
@app.route('/history', methods=['GET'])
def get_history():
    conn = sqlite3.connect('calculations.db')
    cursor = conn.cursor()
    cursor.execute('SELECT num1, num2, operation, result, timestamp FROM history ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()

    history_list = []
    for row in rows:
        history_list.append({
            'num1': row[0],
            'num2': row[1],
            'operation': row[2],
            'result': row[3],
            'timestamp': row[4]
        })

    return jsonify(history_list)

if __name__ == '__main__':
    app.run(debug=True)