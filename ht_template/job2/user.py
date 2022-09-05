import requests


res = requests.post(url='http://localhost:8082/',
                    headers={
                        "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09",
                        "stg_dir": "/path/to/my_dir/stg/sales/2022-08-09"})

if res.ok:
    print(res.json())
else:
    print(res.status_code)
