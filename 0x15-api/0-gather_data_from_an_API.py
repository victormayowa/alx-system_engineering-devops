#!/usr/bin/python3
"""Pthonic API"""
import requests
import sys


def todos(id):
    """exports"""
    user_link = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    user = requests.get(user_link).json()
    todo_link = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    todo_list = requests.get(todo_link).json()
    user = user["username"]
    file = "{}.csv".format(id)
    with open(file, "w") as f:
        for todo in todo_list:
            line = '"{}","{}","{}","{}"\n'.format(
                id,
                user,
                str(todo["completed"]),
                todo["title"]
            )
            f.write(line)


if __name__ == "__main__":
    todos(sys.argv[1])