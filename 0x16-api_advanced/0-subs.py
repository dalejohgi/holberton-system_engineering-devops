#!/usr/bin/python3
"""How many suscribers module"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of suscribers or 0 for invalid subreddit"""
    if not subreddit:
        return 0
    user_agent = {'User-Agent': 'dalejohgi'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=user_agent)
    if response.status_code not in range(200, 300):
        return 0
    response_json = response.json()
    data = response_json["data"]
    return (data["subscribers"])
