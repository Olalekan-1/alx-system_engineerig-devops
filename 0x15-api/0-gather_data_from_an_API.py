#!/usr/bin/python3

""" Gather data from a fake api
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    employee_id = argv[1]
    endpoint1 = f"https://jsonplaceholder.typicode.com/users?id={employee_id}"
    endpoint2 = f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"

    name_response = requests.get(endpoint1).json()
    employee_name = name_response[0]['name']

    tasks_response = requests.get(endpoint2).json()
    total_number_of_task = 0
    completed = 0
    tasks = []

    for dict_ in tasks_response:
        if 'id' in dict_:
            total_number_of_task += 1
        if dict_['completed'] is True:
            completed += 1
            tasks.append(dict_['title'])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed,
                                                          total_number_of_task)
          )
    for task in tasks:
        print("\t {}".format(task))
