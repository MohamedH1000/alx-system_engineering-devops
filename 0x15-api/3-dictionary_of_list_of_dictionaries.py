#!/usr/bin/python3

"""
export data in the json format by this python script
"""

from requests import get
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    new_dict1 = {}

    for b in data2:

        row = []
        for a in data:

            new_dict2 = {}

            if b['id'] == a['userId']:

                new_dict2['username'] = b['username']
                new_dict2['task'] = a['title']
                new_dict2['completed'] = a['completed']
                row.append(new_dict2)

        new_dict1[b['id']] = row

    with open("todo_all_employees.json",  "w") as f:

        json_obj = json.dumps(new_dict1)
        f.write(json_obj)
