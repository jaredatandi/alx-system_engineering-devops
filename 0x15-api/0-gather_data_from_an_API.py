#!/usr/bin/python3
""" A module to get todo list
"""


import requests
import sys

# Set up the API endpoint URL
url = 'https://jsonplaceholder.typicode.com/todos'

# Get the employee ID from the command line arguments
employee_id = sys.argv[1]

# Create the request URL to get the employee's TODO list
employee_todo_url = f'{url}?userId={employee_id}'

# Send a GET request to the API and store the response
response = requests.get(employee_todo_url)

# Convert the response JSON to a Python list of dictionaries
employee_todo_list = response.json()

# Count the number of completed and total tasks
completed_tasks = 0
total_tasks = len(employee_todo_list)

# Create a list to store the titles of completed tasks
completed_task_titles = []

for task in employee_todo_list:
    if task['completed']:
        completed_tasks += 1
        completed_task_titles.append(task['title'])

# Get the employee name by sending a GET request to the users API endpoint
user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
user_response = requests.get(user_url)
user_data = user_response.json()
employee_name = user_data['name']

# Display the results
print(f'Employee {employee_name} is done
      with tasks({completed_tasks}/{total_tasks}): ')
for title in completed_task_titles:
    print('\t ', title)
