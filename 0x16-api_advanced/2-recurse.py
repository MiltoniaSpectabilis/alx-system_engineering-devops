#!/usr/bin/python3
"""
This script fetches all the hot posts in a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Fetches all hot posts of a subreddit recursively"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    if after:
        url += f"?after={after}"
    headers = {'User-Agent': 'SubScraper'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get('data')
    posts = data.get('children')
    if not posts:
        return hot_list if hot_list else None
    hot_list.extend(post['data']['title'] for post in posts)
    after = data.get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
