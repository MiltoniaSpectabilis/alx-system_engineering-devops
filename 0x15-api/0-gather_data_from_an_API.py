#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    user_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    ).json()

    todos_data = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    ).json()

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)

    print(
        f"Employee {employee_name} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
