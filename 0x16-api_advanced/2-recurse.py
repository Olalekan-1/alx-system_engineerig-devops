#!/usr/bin/python3

""" make api request to reddit server
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            if data['data']['after']:
                return recurse(subreddit, hot_list,
                               after=data['data']['after'])
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        elif response.status_code == 302:
            return None
        else:
            return None
    except Exception as e:
        return None
