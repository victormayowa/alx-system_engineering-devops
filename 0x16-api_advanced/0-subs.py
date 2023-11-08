#!/usr/bin/python3
''' interacting with the Reddit API.'''

import requests


def number_of_subscribers(subreddit):
    '''return the number of subscribers'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    ''' Make the API request'''
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
