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

    EmpyeeID = argv[1]
    URLidentty = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(EmpyeeID)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(EmpyeeID)

    employee = sessionReq.get(URLidentty)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    usser = employeeName.json()['username']

    todos = 0

    for dontasks in json_req:
        if dontasks['completed']:
            todos += 1

    fileCSV = EmpyeeID + '.csv'

    with open(fileCSV, "w", newline='') as csvfile:
        write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for intg in json_req:
            write.writerow([EmpyeeID, usser, intg.get('completed'), intg.get('title')])
