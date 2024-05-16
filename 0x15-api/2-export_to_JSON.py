#!/usr/bin/python3
"""
script to retrieve information about an employee's TODO list progress
using REST API.
"""

import json
import requests
import sys

if __name__ == "__main__":
    emp_id = int(sys.argv[1])
    todos_url = f"https://jsonplaceholder.typicode.com/todos/?userId={emp_id}"

    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    all_tasks = [todo for todo in todos]

    users_url = f"https://jsonplaceholder.typicode.com/users/?id={emp_id}"
    users_response = requests.get(users_url)
    users = users_response.json()
    EMPLOYEE_NAME = users[0]['username']

    listing = []
    for task in all_tasks:
        # print(f'\t {emp_id},{EMPLOYEE_NAME},{task['completed']},
        # {task["title"]}')
        itt = [{"task": task["title"],
                "completed": task['completed'],
                "username": EMPLOYEE_NAME}]
        for i in range(len(itt)):
            listing.append(itt[i])
        # print(dummy)
        # listing.append(dummy)
    # print(listing)
    json_dict = {str(emp_id): listing}

    file_name = str(emp_id)+'.json'
    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
