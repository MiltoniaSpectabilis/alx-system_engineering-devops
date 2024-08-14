#!/usr/bin/python3
"""Module to print titles of top 10 hot posts for a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post["data"]["title"])
