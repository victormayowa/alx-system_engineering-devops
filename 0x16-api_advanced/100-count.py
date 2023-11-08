#!/usr/bin/python3
"""
queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, found_list=[], after=None):
    '''
    recursive function that queries the Reddit API
    '''
    user = {'User-agent': 'test45'}
    p = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                     .format(subreddit, after), headers=user)
    if after is None:
        wlist = [word.lower() for word in word_list]

    if p.status_code == 200:
        p = p.json()['data']
        after = p['after']
        p = p['children']
        for post in p:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in wlist:
                    found_list.append(word)
        if aft is not None:
            count_words(subreddit, wlist, found_list, aft)
        else:
            res = {}
            for w in found_list:
                if w.lower() in res.keys():
                    res[w.lower()] += 1
                else:
                    res[w.lower()] = 1
            for key, value in sorted(res.items(), key=lambda item: item[1],
                                     reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
