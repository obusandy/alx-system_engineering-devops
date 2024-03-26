#!/usr/bin/python3
"""
using this REST API, this is a script that, for a given employee ID,
returns information about his/her TODO list progress.
using urllib or requests module
accepts an integer as a parameter, which is the employee ID
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    nameurl = "https://jsonplaceholder.typicode.com/"
    usser = requests.get(nameurl + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(nameurl + "todos", params={"userId": sys.argv[1]}).json()

    done = [t.get("title") for t in todos if t.get("completed") is True]

    # print the results

    print("Employee {} is done with tasks({}/{}):".format(
        usser.get("name"), len(done), len(todos)))
    [print("\t {}".format(c)) for c in done]
