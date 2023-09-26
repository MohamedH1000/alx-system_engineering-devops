#!/usr/bin/python3

"""
export data in csv format by this script
"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for a in data2:
        if a['id'] == int(argv[1]):
            employee = a['username']

    with open(argv[1] + '.csv', 'w', newline='') as file:
        writ = csv.writer(file, quoting=csv.QUOTE_ALL)

        for a in data:

            row = []
            if a['userId'] == int(argv[1]):
                row.append(a['userId'])
                row.append(employee)
                row.append(a['completed'])
                row.append(a['title'])

                writ.writerow(row)
