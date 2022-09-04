"""
Layer of persistence. Save content to outer warld here.
"""
import os
import json


def save_to_disk(sales, path):
    folder = '/'.join(path.split('/')[:len(path.split('/'))-1])[1:] + '/'
    file_name = path.split('/')[len(path.split('/'))-1:][0]
    print(folder, file_name)

    for file in os.listdir(folder):
        os.remove(os.path.join(folder, file))

    with open(folder + f'{file_name}.json', 'w') as f:
        f.write(json.dumps(sales))
