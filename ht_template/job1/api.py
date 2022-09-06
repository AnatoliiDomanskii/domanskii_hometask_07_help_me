import requests


def get_sales(date: str, auth_token):

    url = f'https://fake-api-vycpfa6oca-uc.a.run.app/sales?date={date}&page=1'  # move parameters to link
    i = 1  # download page counter
    arr_sales = []  # list for result

    while True:
        res = requests.get(
            url=url[:len(url) - 1] + str(i),  # take data from API, where i is number of page
            headers={'Authorization': auth_token})  # use toker for downloading

        i += 1  # move to next page

        if res.ok:
            arr_sales += res.json()  # save answer from API to list while code_status is true (200, 201)
        else:
            print(f'Downloaded {i - 2} pages.')
            return arr_sales, res.status_code  # return list with sales

