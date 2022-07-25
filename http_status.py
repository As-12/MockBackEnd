import random

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/http_status/<int:code>')
def echo_code(code):
	return '', code

if __name__ == '__main__':
	app.run()

	