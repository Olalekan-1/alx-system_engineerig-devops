#!/usr/bin/python3

""" Gather data from a fake api and exports
    to a csv file
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    all_data = {}
    file_name = "todo_all_employees.json"
    endpoint = "https://jsonplaceholder.typicode.com/users"
    all_user_request = requests.get(endpoint).json()
    for dictt in all_user_request:
        if 'id' in dictt:
            employee_id = dictt['id']
            a = employee_id
        endpoint1 = f"https://jsonplaceholder.typicode.com/users?id={a}"
        endpoint2 = f"https://jsonplaceholder.typicode.com/todos?userId={a}"

        name_response = requests.get(endpoint1).json()
        employee_name = name_response[0]['username']

        tasks_response = requests.get(endpoint2).json()
        # all_data = {}
        # file_name = "todo_all_employees.json"
        list_data = []
        for dict_ in tasks_response:
            dict_data = {"username": employee_name, "task": dict_['title'],
                         "completed": dict_['completed'],
                         }
            list_data.append(dict_data)
            all_data[employee_id] = list_data
            with open(file_name, mode='w') as file:
                json.dump(all_data, file)
