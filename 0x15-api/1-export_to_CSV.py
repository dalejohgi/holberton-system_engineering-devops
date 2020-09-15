#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == "__main__":
    import requests
    from sys import argv

    file_path = argv[1] + ".csv"
    api_url = "https://jsonplaceholder.typicode.com"
    user = requests.get('{}/users/{}'.format(api_url, argv[1])).json()
    tds = requests.get('{}/todos/?userId={}'.format(api_url, argv[1])).json()
    tds_done = requests.get('{}/todos/?userId={}&completed=true'
                            .format(api_url, argv[1])).json()

    user_name = user.get('username')
    with open(file_path, 'a') as f:
        for tasks in tds:
            f.write("\"{}\",\"{}\",\"{}\",\"{}\"\n"
                    .format(argv[1],
                            user_name,
                            tasks.get('completed'),
                            tasks.get('title')))
