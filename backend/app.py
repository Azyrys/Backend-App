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
    role = user_data.get('role')

    if username and password:
        # Add user to the database
        database.add_user(username, password, role)
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


@app.route('/topics', methods=['GET'])
def get_topics():
    topics = database.get_all_topics()
    
    return jsonify(topics)


@app.route('/add-post', methods=['POST'])
def add_new_post():
    data = request.get_json()
    topic = data.get('topic')
    content = data.get('content')

    if not topic or not content:
        return jsonify({'message': 'Topic and content are required.'}), 400

    # Check if the topic exists
    topic_id = database.get_topic_id(topic)
    if not topic_id:
        return jsonify({'message': 'Topic does not exist.'}), 404

    # Add the post to the database
    database.add_post(content, topic_id)

    return jsonify({'message': 'Post added successfully.'}), 201

@app.route('/add-topic', methods=['POST'])
def add_new_topic():
    data = request.get_json()
    content = data.get('content')

    if not content:
        response = jsonify({'message': 'Content is required.'})
        response.status_code = 400
        response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')  # Replace with your frontend URL
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response

    # Add the post to the database
    database.add_topic(content)

    response = jsonify({'message': 'Topic added successfully.'})
    response.status_code = 201
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')  # Replace with your frontend URL
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

if __name__ == '__main__':
    app.run()