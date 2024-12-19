from flask import Flask, jsonify, request
from fetch import fetch_user_data
from insert import create_database, insert_user_data
from queries import sort_records_by_name, update_email, filter_users_by_longitude
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    user_data = fetch_user_data()
    if user_data:
        return user_data
    return jsonify({"message": "Failed to retrieve data"}), 500

@app.route('/create_db', methods=['POST'])
def create_db():
    try:
        create_database()
        return jsonify({"message": "Database and tables created successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/insert_data', methods=['POST'])
def insert_data():
    user_data = fetch_user_data()
    if user_data:
        insert_user_data(user_data)
        return jsonify({"message": "User data inserted successfully"})
    return jsonify({"message": "Failed to fetch user data"}), 500

@app.route('/sort_data', methods=['GET'])
def sort_data():
    try:
        sorted_data = sort_records_by_name()
        return sorted_data
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/update_email', methods=['POST'])
def update_email_route():
    user_id = request.json.get('user_id')
    new_email = request.json.get('new_email')
    try:
        message = update_email(user_id, new_email)
        return jsonify({"message": str(message)})
        # return jsonify({"message": f"Email for user {user_id} updated successfully"})
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/filter_users', methods=['POST'])
def filter_users():
    min_longitude = request.json.get('min_longitude')
    try:
        filtered_users = filter_users_by_longitude(min_longitude)
        return filtered_users
    except Exception as e:
        return jsonify({"message": str(e)}), 500

if __name__ == '__main__':
    port_number = 5000
    app.run(debug=True, port = port_number)
