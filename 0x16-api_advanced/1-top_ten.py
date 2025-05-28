#!/usr/bin/python3
"""
This script fetches the number of subscribers in a subreddit
"""

import requests


def top_ten(subreddit):
    """Fetches the 10 first hot posts from a given subreddit"""
    # use custom header to avoid error message
    headers = {'User-Agent': 'DataScrapingTest by Hamid'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        children = data.get('data').get('children')
        for title in children[:10]:
            print(title.get('data').get('title'))
    else:
        print(None)
