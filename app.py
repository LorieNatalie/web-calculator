from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = float(data['num1'])
    num2 = float(data['num2'])
    operation = data['operation']

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

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)