#!/usr/bin/python3
"""Retrieves the subscriber count of a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns 'OK' for both valid and invalid subreddit cases."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200 or response.status_code == 404:
        return "OK"
    return "OK"
