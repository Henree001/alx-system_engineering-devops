#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()
    completed_tasks = [[sys.argv[1], user.get('username'),
                       item.get('completed'), item.get('title')]
                       for item in todos]

    with open('{}.csv'.format(sys.argv[1]), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(completed_tasks)
