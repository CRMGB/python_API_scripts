import json
import re

from urllib.request import Request, urlopen

AGENT = 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'
URL = "https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10"

class GetAuthorsAndBooks:
    def get_values(self):
        req = Request(
            URL, headers={
                'User-Agent': AGENT
            }
        )
        data = json.loads(urlopen(req).read().decode('utf-8'))
        names_and_books = self.__extract_names_and_books(data)
        return names_and_books

    def __extract_names_and_books(self, data):
        data_list = []
        list_names = []
        books_list = []        
        for key in data["data"]:
            if key["attributes"] or key["relationships"]:
                data_list.append(key["attributes"])
                data_list.append(key["relationships"])
        for dic in data_list:
            for key, val in dic.items():
                if key == 'books':
                    books_list.append(
                        sum(1 for d in val['data'] if d.get('id'))
                    )
                if key == 'name':
                    list_names.append(
                        {'name': val}
                    )
        
        return self.__update_with_books(list_names, books_list)

    def __update_with_books(self, list_names, books_list):
        i = 0
        for item in list_names:
            item.update({"book_count": books_list[i]})
            i += 1
        return list_names
