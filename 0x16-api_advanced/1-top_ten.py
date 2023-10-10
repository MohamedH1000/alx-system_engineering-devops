#!/usr/bin/python3
"""
print the first 10 title of a hot post
by this function
"""

import requests


def top_ten(subreddit):
    """
    reddit api ti be quered
    and to print the top 10 title
    by this function
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
