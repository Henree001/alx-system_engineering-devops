#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(sys.argv[1])).json()
    user_details = []
    for item in todos:
        dic = {}
        for key, value in item.items():
            if key == 'title':
                dic['task'] = value
            if key == 'completed':
                dic['completed'] = value
        dic['username'] = user.get('username')
        user_details.append(dic)
    data = {sys.argv[1]: user_details}

    with open('{}.json'.format(sys.argv[1]), 'w') as file:
        json.dump(data, file)
