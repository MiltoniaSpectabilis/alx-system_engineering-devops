#!/usr/bin/python3
"""
Module to query Reddit API for subscriber count.
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Linux x86_64) Edge109.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
