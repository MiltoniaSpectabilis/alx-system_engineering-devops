#!/usr/bin/python3
"""Module to count occurrences of keywords in subreddit hot post titles."""
import requests


def count_words(subreddit, word_list, after='', word_dict=None):
    """Count occurrences of keywords in subreddit hot post titles."""
    if word_dict is None:
        word_dict = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    for post in data.get("children", []):
        title = post["data"]["title"].lower().split()
        for word in word_dict:
            word_dict[word] += title.count(word)

    after = data.get("after")
    if after:
        count_words(subreddit, word_list, after, word_dict)
    else:
        sorted_words = sorted(
            [(k, v) for k, v in word_dict.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_words:
            print(f"{word}: {count}")
