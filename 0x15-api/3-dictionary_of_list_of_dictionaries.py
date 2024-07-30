#!/usr/bin/python3
"""
Gather data from an API and export to JSON
"""

import json
import requests

if __name__ == "__main__":

    base_url = 'https://jsonplaceholder.typicode.com'

    # Fetch all users
    users_data = requests.get(f'{base_url}/users').json()

    # Prepare data for JSON export
    all_tasks = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch todos for the user
        todos_data = requests.get(f'{base_url}/users/{user_id}/todos').json()

        tasks_list = []
        for task in todos_data:
            tasks_list.append({
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

        all_tasks[user_id] = tasks_list

    # Export data to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)
