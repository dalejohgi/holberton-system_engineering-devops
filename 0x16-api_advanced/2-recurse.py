#!/usr/bin/python3
"""Hot recurse module"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of the hot subreddits or 0 for invalid subreddit"""
    if not subreddit:
        return None
    user_agent = {'User-Agent': 'dalejohgi'}
    parameters = {'after': after, 'limit': 100}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=user_agent, params=parameters)
    if response.status_code not in range(200, 300):
        return None
    response_json = response.json()
    after = response_json['data']['after']
    elements = response_json['data']['children']
    for element in elements:
            hot_list.append(element['data']['title'])
    if after is None:
        return hot_list
    else:
        return (recurse(subreddit, hot_list, after))
