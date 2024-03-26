#!/usr/bin/python3
"""
This is a script that records all tasks that are owned by this employee.
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
    usr = employeeName.json()['username']

    todos = []
    updatedUsser = {}

    for all_Emplys in json_req:
        todos.append(
            {
                "task": all_Emplys.get('title'),
                "completed": all_Emplys.get('completed'),
                "username": usr,
            })
    updatedUsser[EmpyeeID] = todos

    file_Json = EmpyeeID + ".json"
    with open(file_Json, 'w') as files:
        json.dump(updatedUsser, files)
