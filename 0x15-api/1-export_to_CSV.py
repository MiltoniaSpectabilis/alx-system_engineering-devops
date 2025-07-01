#!/usr/bin/python3

"""API Exercise
"""

import csv
import requests
from sys import argv

if __name__ == '__main__':
    id = argv[1]
    tasks_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    names_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    tasks_data = requests.get(tasks_url).json()
    names_data = requests.get(names_url).json()

    user_name = names_data.get('username')

    csv_filename = f'{id}.csv'

    with open(csv_filename, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            csv_writer.writerow([
                id,
                user_name,
                task.get('completed'),
                task.get('title')
            ])
