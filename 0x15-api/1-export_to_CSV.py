#!/usr/bin/python3

""" Gather data from a fake api and exports
    to a csv file
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    employee_id = argv[1]
    endpoint1 = f"https://jsonplaceholder.typicode.com/users?id={employee_id}"
    endpoint2 = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    name_response = requests.get(endpoint1).json()
    employee_name = name_response[0]['name']

    tasks_response = requests.get(endpoint2).json()
    all_data = []
    file_name = f"{employee_id}.csv"

    for dict_ in tasks_response:
        row_data = [employee_id, employee_name,
                    dict_.get('completed'),
                    dict_.get('title')
                    ]
        all_data.append(row_data)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(all_data)
