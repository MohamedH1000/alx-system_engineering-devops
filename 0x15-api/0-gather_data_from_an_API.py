#!/usr/bin/python3

"""
a python script that takes the empolyees id
and return the information about him in the todolist
"""

from requests import get
from sys import argv


if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    completed = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for a in data2:
        if a.get('id') == int(argv[1]):
            employee = a.get('name')

    for a in data:
        if a.get('userId') == int(argv[1]):
            total += 1

            if a.get('completed') is True:
                completed += 1
                tasks.append(a.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee, completed,
                                                          total))

    for a in tasks:
        print("\t {}".format(a))
