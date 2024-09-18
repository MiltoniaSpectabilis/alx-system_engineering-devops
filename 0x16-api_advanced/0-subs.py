#!/usr/bin/python3
"""Retrieves the subscriber count of a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0."""
    # Define the URL for the subreddit about page
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    # Set a custom User-Agent to avoid being blocked
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditAPI/1.0)'}
    try:
        # Make the GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check if the status code indicates success (200)
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If status is not 200, it likely means invalid subreddit
            return 0
    except requests.RequestException:
        # In case of network or other request-related errors, return 0
        return 0
