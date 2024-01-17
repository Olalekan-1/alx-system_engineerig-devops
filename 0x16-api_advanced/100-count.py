#!/usr/bin/python3

""" Make an api request to  reddit server
"""

from collections import Counter
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = Counter()
    if after is None:
        after = ''

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()

            titles = [post['data']['title'].lower() for
                      post in data['data']['children']]

            for word in word_list:
                counts[word] += sum(title.count(f' {word} ') for
                                    title in titles)

            if data['data']['after']:
                return count_words(subreddit, word_list,
                                   after=data['data']['after'], counts=counts)
            else:
                sorted_counts = sorted(counts.items(),
                                       key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        elif response.status_code == 404:
            pass
        elif response.status_code == 302:
            pass
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
