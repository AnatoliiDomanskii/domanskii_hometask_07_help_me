"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
from flask import Flask, request
from flask import typing as flask_typing

import api
import storage

AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    auth_token = request.headers['Authorization']
    data = request.headers['data']
    raw_dir = request.headers['raw_dir']


    # storage.save_to_disk()
    print(data)
    return {
               'sales': api.get_sales(data, auth_token)

           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)

