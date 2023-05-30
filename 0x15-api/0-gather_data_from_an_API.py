#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()
    completed_tasks = [item.get('title') for item in todos
                       if item.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
          user.get("name"), len(completed_tasks), len(todos)))
    for item in completed_tasks:
        print('\t {}'.format(item))
