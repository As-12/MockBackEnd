import random

from flask import Flask, request, jsonify

app = Flask(__name__)

mock_data: list = []
page_size: int = 25
data_size: int = 700

def new_employee(id: int):
    result = {"name": "Mr " + str(id), "id": id}
    return result

def populate_mock_data():
    for i in range(page_size):
        mock_data.append({})
        mock_data[i]["employee_data"] = [new_employee(random.randint(0, 1000)) for i in range(page_size)]
        mock_data[i]["page_size"] = page_size
        mock_data[i]["page"] = i + 1
        mock_data[i]["page_count"] = page_count
        mock_data[i]["employee_count"] = page_count * page_size

@app.route('/')
def default():
    return '', 204

@app.route('/employees')
def list_employee_page():
    index: int = int(request.args.get("page"))
    if index <= 0 or index > 25:
        return '', 204
    else:
        return mock_data[index - 1]


if __name__ == '__main__':
    populate_mock_data()
    app.run()

