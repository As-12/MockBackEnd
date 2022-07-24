import random

from flask import Flask, request, jsonify

app = Flask(__name__)

mock_data = {}

def new_employee(id: int):
    result = {"name": "Mr " + id, "id": id}
    return result

def populate_mock_data():
    for i in range(25):
        mock_data.append({})
        mock_data[i]["employee_data"] = [new_employee(i) for i in range(25)]
        mock_data["page_size"] = 25
        mock_data["page"] = i + 1
        mock_data["page_count"] = 25
        mock_data["employee_count"] = 25 * 25

@app.route('/')
def default():
    return '', 204

@app.route('/employee')
def list_employee_page():
    return '', 204

if __name__ == '__main__':
    populate_mock_data()
    app.run()
