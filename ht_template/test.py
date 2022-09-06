import requests
import unittest


class TestCircleArea(unittest.TestCase):

    def test_return_400_path_param_missed(self):
        """return 400 if param missed"""
        res = requests.post(
            url=f'http://localhost:8081/',
            json={
                "date": "2022-08-09"
            })

        self.assertEqual(400, res.status_code)

    def test_return_400_date_param_missed(self):
        """return 400 if param missed"""
        res = requests.post(
            url=f'http://localhost:8081/',
            json={
                "raw_dir": "D:/robot_dreams/1/lect_02/ht_template/job1/path/to/my_dir/raw/sales/2022-08-09"
            })

        self.assertEqual(400, res.status_code)

    def test_currect_request(self):
        """check status_code with correct request. should be 201"""
        res = requests.post(
            url=f'http://localhost:8081/',
            json={
                "date": "2022-08-09",
                "raw_dir": "D:/robot_dreams/1/lect_02/ht_template/job1/path/to/my_dir/raw/sales/2022-08-09"
            })
        self.assertEqual(201, res.status_code)

    def
