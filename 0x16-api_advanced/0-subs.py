#!/usr/bin/python3
"""
This script fetches the number of subscribers in a subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Fetches the subscriber count for a given subreddit"""
    # use custom header to avoid error message
    headers = {'User-Agent': 'DataScrapingTest by Hamid'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data.get('data').get('subscribers')
        return subscribers
    return 0
