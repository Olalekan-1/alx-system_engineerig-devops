#!/usr/bin/python3

"""
make api request to reddit server
"""
import requests


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()

            for post in data['data']['children'][:10]:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
