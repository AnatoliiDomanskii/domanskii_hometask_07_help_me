"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""

# import libs
from flask import Flask, request
from flask import typing as flask_typing

import os

from ht_template.job1 import api
from ht_template.job1 import storage

# create Flask object
app = Flask(__name__)


# create function for job_1
@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    auth_token = os.environ.get('API_AUTH_TOKEN')  # take AUTH_TOKEN
    data = request.json.get('date')  # take data from request to server
    raw_dir = request.json.get('raw_dir')  # take path for save raw data about sales

    if not auth_token:
        print("AUTH_TOKEN environment variable must be set")  # check if auth_token is not null

    if not data or not raw_dir:
        return {
                   "message": "You lost data or raw_dir"
               }, 400

    sales= api.get_sales(data, auth_token)  # use func get_sales() from api for download data from API
    storage.save_to_disk(sales, raw_dir)  # use func save_to_disk for save json file with data from API to raw_dir

    return {
               "message": "Data retrieved successfully from API"  # return message about finish.
           }, 201  # with code 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8081)  # start web server
