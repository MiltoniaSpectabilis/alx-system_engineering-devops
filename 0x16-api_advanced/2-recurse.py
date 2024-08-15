#!/usr/bin/python3
"""Module to recursively fetch all hot post titles from a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot post titles from a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    hot_list.extend(post["data"]["title"] for post in data.get("children", []))
    after = data.get("after")

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
