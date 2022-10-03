"""
Layer of persistence. Save content to outer warld here.
"""
import os
import json


def save_to_disk(sales, path):
    folder = os.path.dirname(path)  # take folder for download

    if os.listdir(folder):  # if folder is NOT empty
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))  # then delete all files from folder

    with open(folder + '/2022-08-09.json', 'w') as f:
        f.write(json.dumps(sales))  # save data with sale to folder with name 2022-08-09.json
