#!/usr/bin/python3

"""
in json format a data to be exported by this script
"""

from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for a in data2:
        if a['id'] == int(argv[1]):
            u_name = i['username']
            id_no = i['id']

    row = []

    for a in data:

        new_dict = {}

        if a['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = a['title']
            new_dict['completed'] = i['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json",  "w") as f:
        f.write(json_obj)
