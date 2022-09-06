"""
Layer of persistence. Save content to outer warld here.
"""
import os
import json


def save_to_disk(sales, path):
    folder = os.path.dirname(path)
    print(path)
    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))

    with open(folder + '/2022-08-09.json', 'w') as f:
        f.write(json.dumps(sales))
