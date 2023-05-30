#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    data = {}
    for user in users:
        user_details = []
        todos = requests.get(url + "users/{}/todos".format(
                             user.get('id'))).json()
        for item in todos:
            dic = {}
            dic['username'] = user.get('username')
            for key, value in item.items():
                if key == 'title':
                    dic['task'] = value
                if key == 'completed':
                    dic['completed'] = value
            user_details.append(dic)
        data[user.get('id')] = user_details

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)
