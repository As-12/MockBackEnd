import math
import random

from flask import Flask, request, jsonify

app = Flask(__name__)

mock_data: list = []
page_size: int = 25
data_size: int = 710
page_count: int = math.ceil(data_size / page_size)


def new_employee(id: int):
    result = {"name": "Mr " + str(id), "id": id}
    return result


def populate_mock_data():
    total: int = 0
    for i in range(page_count - 1):
        mock_data.append({})
        mock_data[i]["employee_data"] = [new_employee(random.randint(0, 1000)) for i in range(page_size)]
        mock_data[i]["page_size"] = page_size
        mock_data[i]["page"] = i + 1
        mock_data[i]["page_count"] = page_count
        mock_data[i]["employee_count"] = data_size
        total += page_size
        print("Populating page " + str(i) + " size: " + str(page_size) + " total: " + str(total) + "/" + str(data_size))
    last_page = page_count - 1
    last_page_count = data_size % page_size
    if last_page_count == 0:
        last_page_count = page_size
    mock_data.append({})
    mock_data[last_page]["employee_data"] = [new_employee(random.randint(0, 1000)) for i in range(last_page_count)]
    mock_data[last_page]["page_size"] = last_page_count
    mock_data[last_page]["page"] = page_count
    mock_data[last_page]["page_count"] = page_count
    mock_data[last_page]["employee_count"] = data_size
    total += last_page_count
    print("Populating page " + str(last_page) + " size: " + str(last_page_count) + " total: " + str(total) + "/"
          + str(data_size))


@app.route('/')
def default():
    return '', 204


@app.route('/employees')
def list_employee_page():
    index: int = int(request.args.get("page"))
    if index <= 0 or index > page_count:
        return '', 204
    else:
        return mock_data[index - 1]


if __name__ == '__main__':
    populate_mock_data()
    app.run()
