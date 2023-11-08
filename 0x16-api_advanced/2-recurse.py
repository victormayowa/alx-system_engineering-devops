#!/usr/bin/python3
"""
queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit1-main
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list."""
    l = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    h = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    p = {"after": after, "count": count, "limit": 100}
    response = requests.get(l, headers=h, params=p,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    res = response.json().get("data")
    after = res.get("after")
    count += res.get("dist")
    for c in res.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
