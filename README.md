Description of the tasks:

JSON API Exercise 1

    Write a Python script that:
    - Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors?
    page[size]=10
    - Parses the JSON response
    - Prints a list of dictionaries containing:
    o Each author’s name in a “name” key
    o The number of books they have written in a “book_count” key


JSON API Exercise 2

    Write a Python script that:
    - Pages through the endpoint below
    - Extends an author_list variable with each page of author data
    - Stops paging when either:
    o There are no more authors
    o 15 pages have been processed
    - Tells the user which condition above stopped the loop
    - Prints the author_list variable
    Starting endpoint: https://jsonapiplayground.reyesoft.com/v2/authors?
    page[size]=10&page[number]=1JSON API Exercise 3
    Write a Python function that:
    - Accepts an author_id parameter
    - Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors/{au-
    thor_id}
    - Parses the JSON response
    - Returns a single dictionary containing:
    -
    o The author name in a “name” key
    o The number of books they have written in a “book_count” key
    Raises a meaningful exception if the author_id is not found
    For bonus points, write a unit test to prove that your function raises the expected exception
    if author_id is not found. You will need to mock the API response to achieve this.

JSON API Exercise 3

    Write a Python function that:
    - Accepts an author_id parameter
    - Sends a GET request to https://jsonapiplayground.reyesoft.com/v2/authors/{au-
    thor_id}
    - Parses the JSON response
    - Returns a single dictionary containing:
    -
    o The author name in a “name” key
    o The number of books they have written in a “book_count” key
    Raises a meaningful exception if the author_id is not found

I'm using v_env, to initialise:
    Install pip first, then:
        To create v_env:
            python3 -m venv my_env

        activate v_env:
            source myvenv/bin/activate

For testing I'm using pytest, to install:
        pip install -U pytest
        see docs: https://docs.pytest.org/en/stable/getting-started.html

For the response test I'm using:
    pip install responses

For testing I cd to script to test, example: 
    cd script_1 and then python -m pytest

I'm solving Exercise 3 in script_1 alongside with the Exercise 1, mocking the request as expected and raising a meaningful exception
