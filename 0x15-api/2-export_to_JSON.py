#!/usr/bin/python3

"""API Exercise
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    names_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    tasks_data = requests.get(tasks_url).json()
    names_data = requests.get(names_url).json()

    user_name = names_data.get('username')
    task_list = []
    for task in tasks_data:
        task_title = task.get('title')
        task_status = task.get('completed')
        task_list.append({
            "task": task_title,
            "completed": task_status,
            "username": user_name
        })
    json_filename = f'{id}.json'
    data_to_file = {
        f"{id}": task_list
    }
    with open(json_filename, 'w') as json_f:
        json.dump(data_to_file, json_f)
