#!/usr/bin/python3
'''Pythonic API'''
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    tasks_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        tasks_response = requests.get(tasks_url)
        user_data = user_response.json()
        tasks_data = tasks_response.json()
        
        if not user_data:
            print("Employee not found")
        else:
            employee_name = user_data.get("name")
            completed_tasks = [task for task in tasks_data if task.get("completed")]
            total_tasks = len(tasks_data)
            num_completed = len(completed_tasks)

            print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed, total_tasks))
            for task in completed_tasks:
                print("\t {}".format(task.get("title")))

    except Exception as e:
        print("An error occurred: {}".format(e))
