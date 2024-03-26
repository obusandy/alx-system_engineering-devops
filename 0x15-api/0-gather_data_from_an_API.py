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

    sessionReq = requests.Session()

    EmpyeeID = argv[1]
    URLidentty = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(EmpyeeID)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(EmpyeeID)

    employee = sessionReq.get(URLidentty)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    Emplyeename = employeeName.json()['name']

    todos = 0
    for done_tasks in json_req:
        if done_tasks['completed']:
            todos += 1



    print("Employee {} is done with tasks({}/{}):".
          format(Emplyeename, todos, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
