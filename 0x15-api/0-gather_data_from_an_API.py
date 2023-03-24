#!/usr/bin/python3

"""
A module to get todo list from a json api
using a custom link
"""

import requests
import sys


url = 'https://jsonplaceholder.typicode.com/todos'

employee_id = sys.argv[1]

employee_todo_url = f'{url}?userId={employee_id}'

response = requests.get(employee_todo_url)

employee_todo_list = response.json()

completed_tasks = 0
total_tasks = len(employee_todo_list)

completed_task_titles = []

for task in employee_todo_list:
    if task['completed']:
        completed_tasks += 1
        completed_task_titles.append(task['title'])

user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
user_response = requests.get(user_url)
user_data = user_response.json()
employee_name = user_data['name']

print(f'Employee {employee_name} is done
      with tasks({completed_tasks}/{total_tasks}): ')
for title in completed_task_titles:
    print('\t ', title)
