"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
from flask import Flask, request
from flask import typing as flask_typing

import os
from pathlib import Path


import api
import storage

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    auth_token = os.environ.get('API_AUTH_TOKEN')
    data = request.json.get('date')
    raw_dir = request.json.get('raw_dir')

    if not auth_token:
        print("AUTH_TOKEN environment variable must be set")

    sales = api.get_sales(data, auth_token)
    storage.save_to_disk(sales, raw_dir)

    return {
               "message": "Data retrieved successfully from API"
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)
