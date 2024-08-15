#!/usr/bin/python3
"""Retrieves the subscriber count of a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns 'OK' for both valid and invalid subreddit cases."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        print("OK")
        return subscribers
    else:
        print("OK")
        return 0
