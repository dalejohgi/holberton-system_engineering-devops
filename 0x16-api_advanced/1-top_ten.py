#!/usr/bin/python3
"""HTop 10 module"""

import requests


def top_ten(subreddit):
    """Print the top 10 subreddits or None for invalid subreddit"""
    if not subreddit:
        print('None')
        return
    user_agent = {'User-Agent': 'dalejohgi'}
    parameters = {'limit': 10}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=user_agent, params=parameters)
    if response.status_code not in range(200, 300):
        print('None')
        return
    response_json = response.json()
    elements_dict = response_json['data']['children']
    for element in elements_dict:
        print(element['data']['title'])
