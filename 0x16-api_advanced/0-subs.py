#!/usr/bin/python3
"""
Module to query Reddit API for subscriber count.
"""
import requests


def number_of_subscribers(subreddit):
    """Return number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot/1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        return 0
    except requests.RequestException:
        return 0
