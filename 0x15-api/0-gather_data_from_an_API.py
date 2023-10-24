#!/usr/bin/python3
'''Pythonic API'''
import requests
import sys


def get_todo_progress(employee_id):
    user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user)
    todo_response = requests.get(todo)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data["name"]
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"    {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
