#!/usr/bin/python3
"""
This is a script that records all tasks that
are owned by this employee
It extends the Python script to export data in the CSV format.
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usser = employeeName.json()['username']

    todos = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            todos += 1

    fileCSV = idEmp + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for intg in json_req:
            write.writerow([idEmp, usser, intg.get('completed'), intg.get('title')])
