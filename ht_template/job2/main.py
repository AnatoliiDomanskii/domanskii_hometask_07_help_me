from flask import Flask, request
from fastavro import parse_schema, writer
import json

app = Flask(__name__)  # create flask object


# create func for convert json to avro and save to new folder
@app.route('/', methods=['POST'])
def main():
    raw_dir = request.json.get('raw_dir')  # take path with raw data from request
    stg_dir = request.json.get('stg_dir')  # take path to save .avro file

    schema = {  # build schema for .avro file
        'name': 'Sales',
        'type': 'record',
        'fields': [
            {'name': 'client', 'type': 'string'},
            {'name': 'purchase_date', 'type': 'string'},
            {'name': 'product', 'type': 'string'},
            {'name': 'price', 'type': 'int'}
        ],
    }
    parsed_schema = parse_schema(schema)  # took from documentation, I don't know why I should to do it.
    with open(raw_dir + '.json', 'r') as file_in:  # take file with .json format
        records = json.load(file_in)
        print(records)
        with open(stg_dir + '.avro', 'wb') as out:
            writer(out, parsed_schema, records)  # save data from file with raw data to new .avro file

    return {
               "message": "Data retrieved successfully from API"  # return message about finish.
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)  # start web server
