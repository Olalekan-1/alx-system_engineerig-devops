#!/usr/bin/python3

""" Gather data from a fake api and exports
    to a csv file
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    employee_id = argv[1]
    endpoint1 = f"https://jsonplaceholder.typicode.com/users?id={employee_id}"
    endpoint2 = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    name_response = requests.get(endpoint1).json()
    employee_name = name_response[0]['username']

    tasks_response = requests.get(endpoint2).json()
    all_data = {}
    file_name = f"{employee_id}.json"
    list_data = []

    for dict_ in tasks_response:
        dict_data = {"task": dict_['title'], "completed": dict_['completed'],
                     "username": employee_name
                     }
        list_data.append(dict_data)

    all_data[employee_id] = list_data
    with open(file_name, mode='w') as file:
        json.dump(all_data, file)
