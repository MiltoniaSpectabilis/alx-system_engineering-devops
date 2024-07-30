#!/usr/bin/python3
"""
Gather data from an API
"""
import json
import requests
import sys

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    base_url = 'https://jsonplaceholder.typicode.com'
    user_data = requests.get(f'{base_url}/users/{employee_id}').json()
    todos_data = requests.get(f'{base_url}/users/{employee_id}/todos').json()

    employee_name = user_data.get('name')

    tasks_list = []
    for task in todos_data:
        tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    json_data = {str(employee_id): tasks_list}

    json_filename = f"{employee_id}.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(json_data, json_file)
