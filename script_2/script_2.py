import json
import re

from urllib.request import Request, urlopen

AGENT = 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'
URL = "https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10&page[number]="

class GetPages:
    def get_values(self):
        names_authors = []
        for page in range(1, 15):
            req = Request(
                f'{URL}{page}', headers={
                    'User-Agent': AGENT
                }
            )
            data = json.loads(urlopen(req).read().decode('utf-8'))
            if not data["data"]:
                print("There are no more authors")
                break
            names_authors.append(self.__extract_names_and_books(data, page))
            if page == 15:
                print("15 pages have been processed")
            print(json.dumps(names_authors))
        return names_authors

    def __extract_names_and_books(self, data, page):
        my_list = []
        my_list_2 = []
        for key in data["data"]:
            if key["attributes"]:
                my_list.append(key["attributes"])
        for dic in my_list:
            for key, val in dic.items():
                if key == 'name':
                    my_list_2.append(
                        {'name': val}
                    )
        my_list_2.append({'page': page})
        return my_list_2
