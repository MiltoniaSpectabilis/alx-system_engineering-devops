#!/usr/bin/python3

"""API Exercise
"""

import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    names_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    tasks_data = requests.get(tasks_url).json()
    names_data = requests.get(names_url).json()
    # get completed tasks
    completed_tasks = [task.get('title')
                       for task in tasks_data if task.get('completed')]
    # get user name
    user_name = names_data.get('name')
    # calculate num of completed_tasks
    num_completed_tasks = len(completed_tasks)
    # calculate num of all tasks
    num_all_tasks = len(tasks_data)
    print(f'Employee {user_name} is done with tasks({
        num_completed_tasks}/{num_all_tasks}):')
    for c_task in completed_tasks:
        print('\t', c_task)
