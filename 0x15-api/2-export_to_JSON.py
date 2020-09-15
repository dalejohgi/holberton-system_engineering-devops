#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    file_path = argv[1] + ".json"
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get('{}/users/{}'.format(api_url, argv[1])).json()
    tds = requests.get('{}/todos/?userId={}'.format(api_url, argv[1])).json()
    tds_done = requests.get('{}/todos/?userId={}&completed=true'
                            .format(api_url, argv[1])).json()

    user_name = user.get('username')
    task_list = []
    dic_obj = {}
    for task in tds:
        task_dic = {}
        task_dic["task"] = task.get('title')
        task_dic["username"] = user_name
        task_dic["completed"] = task.get('completed')
        task_list.append(task_dic)
    dic_obj[argv[1]] = task_list
    with open(file_path, 'a') as f:
        json.dump(dic_obj, f)
    print(file_path)
