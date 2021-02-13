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
        my_list = []
        my_list_2 = []
        my_list_3 = []        
        for key in data["data"]:
            if key["attributes"] or key["relationships"]:
                my_list.append(key["attributes"])
                my_list.append(key["relationships"])
        for dic in my_list:
            for key, val in dic.items():
                print(key, val)
                if key == 'books':
                    my_list_3.append(
                        sum(1 for d in val['data'] if d.get('id'))
                    )
                if key == 'name':
                    my_list_2.append(
                        {'name': val}
                    )
        
        return self.__update_with_books(my_list_2, my_list_3)

    def __update_with_books(self, my_list_2, my_list_3):
        i = 0
        for item in my_list_2:
            item.update({"book_count": my_list_3[i]})
            i += 1
        return my_list_2
