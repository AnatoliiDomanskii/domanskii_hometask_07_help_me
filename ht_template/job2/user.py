import requests


res = requests.post(url='http://localhost:8082/',
                    headers={
                        "raw_dir": "D:/robot_dreams/1/lect_02/ht_template/job1/path/to/my_dir/raw/sales/2022-08-09",
                        "stg_dir": "D:/robot_dreams/1/lect_02/ht_template/job1/path/to/my_dir/stg/sales/2022-08-09"})

if res.ok:
    print(res.content)
else:
    print(res.status_code)
