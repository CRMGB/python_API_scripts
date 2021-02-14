import json

from urllib.request import Request, urlopen

AGENT = 'Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36'
URL = "https://jsonapiplayground.reyesoft.com/v2/authors?page[size]=10"
URL_AUTHOR = "https://jsonapiplayground.reyesoft.com/v2/authors/"

class GetAuthorsAndBooks:
    def fetch_data(self, author_id=None):
        if author_id is not None:
            req = Request(
                f'{URL_AUTHOR}{author_id}', headers={
                    'User-Agent': AGENT
                }
            )
        else:
            req = Request(
                URL, headers={
                    'User-Agent': AGENT
                }
            )            
        authors_and_books = self.__select_data(
            json.loads(urlopen(req).read().decode('utf-8')), author_id
        )
        print(json.dumps(authors_and_books))
        return authors_and_books



    def __select_data(self, data, author_id):
        data_list = []
        if author_id:
            for key, val in data["data"].items():
                if key == "attributes" or key == "relationships":
                    data_list.append(val)
            return self.__extract_author_and_books(data_list)[0]

        else:        
            for key in data["data"]:
                if key["attributes"] or key["relationships"]:
                    data_list.append(key["attributes"])
                    data_list.append(key["relationships"])
            return self.__extract_author_and_books(data_list)

            

    def __extract_author_and_books(self, data_list):
        list_names = []
        books_list = []        
        for dic in data_list:
            for key, val in dic.items():
                if key == 'name':
                    list_names.append(
                        {'name': val}
                    )
                if key == 'books':
                    books_list.append(
                        sum(1 for d in val['data'] if d.get('id'))
                    )
        return self.__update_with_books(list_names, books_list)

    def __update_with_books(self, list_names, books_list):
        i = 0
        for item in list_names:
            item.update({"book_count": books_list[i]})
            i += 1
        return list_names
