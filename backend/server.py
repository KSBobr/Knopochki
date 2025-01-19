from flask import Flask, request, jsonify

app = Flask(__name__)

# Словарь для хранения пользователей
users = {}

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    return f'Hello, {name}!'

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    return jsonify({'message': 'Data received', 'data': data})

@app.route('/register', methods=['POST'])
def register():
    # Получаем данные из запроса
    data = request.json
    login = data.get('login')
    password = data.get('password')

    # Проверка на наличие логина
    if login in users:
        return jsonify({'message': 'User already exists!'}), 400

    # Сохраняем пользователя
    users[login] = password
    return jsonify({'message': 'User registered successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)