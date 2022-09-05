import requests


res = requests.post(url='http://localhost:8081/',
                    headers={
                        "data": "2022-08-09",
                        "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"})

if res.ok:
    print(res.json())
else:
    print(res.status_code)
