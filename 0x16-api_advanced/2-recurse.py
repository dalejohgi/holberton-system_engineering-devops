#!/usr/bin/python3
"""Hot recurse module"""

import requests


def recurse(subreddit, hot_list=[]):
    """Return a list of the hot subreddits or 0 for invalid subreddit"""
    if not subreddit:
        return None
    user_agent = {'User-Agent': 'dalejohgi'}
    parameters = {'after': 'after', 'limit': 100}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=user_agent, params=parameters)
    if response.status_code not in range(200, 300):
        return None
    response_json = response.json()
    elements_dict = response_json['data']['children']
    if len(response_json) == 0:
        return (hot_list)
    else:
        for element in elements_dict:
            hot_list.append(element['data']['title'])
        print(len(hot_list))
        recurse(subreddit, hot_list)
