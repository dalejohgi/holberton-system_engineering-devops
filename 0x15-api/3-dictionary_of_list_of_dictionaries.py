#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    file_path = "todo_all_employees.json"
    api_url = "https://jsonplaceholder.typicode.com"
    users = requests.get('{}/users'.format(api_url)).json()
    dic_obj = {}
    for uid in range(1, len(users) + 1):
        tds = requests.get('{}/todos/?userId={}'.format(api_url, uid)).json()
        user = requests.get('{}/users/{}'.format(api_url, uid)).json()
        user_name = user.get('username')
        task_list = []
        for task in tds:
            task_dic = {}
            task_dic["username"] = user_name
            task_dic["task"] = task.get('title')
            task_dic["completed"] = task.get('completed')
            task_list.append(task_dic)
        dic_obj[uid] = task_list
    with open(file_path, 'a') as f:
        json.dump(dic_obj, f)
    print(file_path)
