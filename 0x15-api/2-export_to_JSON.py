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
    # total_tasks = len(todos_data)
    # completed_tasks = [task for task in todos_data if task.get('completed')]
    # number_of_done_tasks = len(completed_tasks)
    #
    # print(
    #     f"Employee {employee_name} is done with tasks"
    #     f"({number_of_done_tasks}/{total_tasks}):"
    # )
    # for task in completed_tasks:
    #     print(f"\t {task.get('title')}")

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
