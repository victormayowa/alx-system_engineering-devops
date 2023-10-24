"""#!/usr/bin/python3
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
    get_todo_progress(employee_id)"""

#!/usr/bin/python3
"""gets todo info and export it to a csv file"""
import requests
import sys


def export_todo(id):
    """exports todo to a csv"""
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(user_url).json()
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todos = requests.get(todo_url).json()
    user_name = user["username"]
    file_name = "{}.csv".format(id)
    with open(file_name, "w") as f:
        for todo in todos:
            row = '"{}","{}","{}","{}"\n'.format(
                id,
                user_name,
                str(todo["completed"]),
                todo["title"]
            )
            f.write(row)


if __name__ == "__main__":
    export_todo(sys.argv[1])