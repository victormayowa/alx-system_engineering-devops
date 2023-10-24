#!/usr/bin/python3
'''export to csv'''
import requests
import sys
import csv


def export_to_csv(employee_id):
    user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user)
    todo_response = requests.get(todo)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_id = user_data["id"]
    employee_name = user_data["username"]

    file_name = f"{employee_id}.csv"

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['USER_ID', 'USERNAME',
                         'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in todo_data:
            task_id = task["id"]
            completed = task["completed"]
            title = task["title"]

            writer.writerow([employee_id, employee_name, completed, title])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    export_to_csv(employee_id)
