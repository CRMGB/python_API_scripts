import json
import re

from urllib.request import Request, urlopen

AGENT = 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'
URL = "https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10&page[number]=1"

class GetPages:
    def get_values(self):
        req = Request(
            URL, headers={
                'User-Agent': AGENT
            }
        )
        data = json.loads(urlopen(req).read().decode('utf-8'))
        print(urlopen(req).read().decode('utf-8'))
        #names_and_books = self.__extract_names_and_books(data)
        #return names_and_books
