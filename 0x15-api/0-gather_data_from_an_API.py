#!/usr/bin/python3
"""
script to retrieve information about an employee's TODO list progress
using REST API.
"""

import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    todos_url = f"https://jsonplaceholder.typicode.com/todos/?userId={emp_id}"
    todos_response = requests.get(todos_url)

    todos = todos_response.json()
    TOTAL_NUMBER_OF_TASKS = len(todos)

    done_tasks = [todo for todo in todos if todo["completed"]]
    NUMBER_OF_DONE_TASKS = len(done_tasks)

    users_url = f"https://jsonplaceholder.typicode.com/users/?id={emp_id}"
    users_response = requests.get(users_url)
    users = users_response.json()
    EMPLOYEE_NAME = users[0]['name']

    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for done_task in done_tasks:
        print(f'\t {done_task["title"]}')
