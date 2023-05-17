from utils import database
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE = 'users.db'  # SQLite database file path

database.create_table()

# Example route for registration
@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    if username and password:
        # Add user to the database
        database.add_user(username, password)
        response = jsonify({'message': 'Registration successful'})
        response.status_code = 200
    else:
        response = jsonify({'message': 'Registration failed'})
        response.status_code = 400

    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')  # Replace with your frontend URL
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

# Example route for retrieving all users
@app.route('/users', methods=['GET'])
def get_users():
    users = database.get_all_users()

    # Convert users to a list of dictionaries
    user_list = [{'id': user[0], 'username': user[1], 'password': user[2]} for user in users]

    response = jsonify(user_list)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')  # Replace with your frontend URL
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


@app.route('/login', methods=['POST'])
def login():
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    if username and password:
        # Retrieve user from the database
        user = database.get_user_by_username(username)

        if user and user[2] == password:
            # Login success
            response = jsonify({'message': 'Login successful'})
            response.status_code = 200
        else:
            # Login failed
            response = jsonify({'message': 'Login failed'})
            response.status_code = 401
    else:
        # Login failed
        response = jsonify({'message': 'Login failed'})
        response.status_code = 401

    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')  # Replace with your frontend URL
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


if __name__ == '__main__':
    app.run()