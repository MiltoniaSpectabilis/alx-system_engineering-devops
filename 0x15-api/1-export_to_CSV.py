#!/usr/bin/python3
"""
Gather data from an API
"""

import requests
import sys
import csv

if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    base_url = 'https://jsonplaceholder.typicode.com'
    user_data = requests.get(f'{base_url}/users/{employee_id}').json()
    todos_data = requests.get(f'{base_url}/users/{employee_id}/todos').json()

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

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([
                employee_id,
                employee_name,
                task.get('completed'),
                task.get('title')
            ])
