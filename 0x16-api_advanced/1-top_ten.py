#!/usr/bin/python3
"""
queries the Reddit API
"""

import requests


def top_ten(subreddit):
    '''prints the titles of the first 10 hot posts listed'''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    '''Adding a custom User-Agent to prevent Too Many Requests error'''
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
