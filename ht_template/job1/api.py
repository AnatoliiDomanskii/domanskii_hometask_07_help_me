
import requests


def get_sales(date: str, auth_token):
    AUTH_TOKEN = auth_token
    print(AUTH_TOKEN)
    url = f'https://fake-api-vycpfa6oca-uc.a.run.app/sales?date={date}&page=1'
    i = 1
    arr_sales = []

    while True:
        res = requests.get(
            url=url[:len(url) - 1] + str(i),
            headers={'Authorization': AUTH_TOKEN})
        print(res.status_code)
        i += 1

        if res.ok:
            arr_sales += res.json()
        else:
            print(f'Downloaded {i - 2} pages.')
            return arr_sales

