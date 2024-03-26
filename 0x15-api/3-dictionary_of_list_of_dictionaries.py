#!/usr/bin/python3
"""
This is a scrit that reacords all tasks from all employees
It extends the  Python script to export data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    tasktodos = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasktodos = tasktodos.json()
    todolist = {}

    """
    prints list
    """

    for usr in users:
        taskList = []
        for task in tasktodos:
            if task.get('userId') == usr.get('id'):
                taskDict = {"username": usr.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todolist[usr.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as filess:
        json.dump(todolist, filess)
