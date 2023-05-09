#!/usr/bin/python3
"""
A function to query Reddit API and return the top 10 titles
if an invalid subreddit is given, the function should return
None
"""

import requests


def top_ten(subreddit):
    """Returns top 10 titles"""
    link = "https://www.reddit.com/r/{}/.json".format(subreddit)
    auth = {
            "User-Agent": "subs:v1.0.0 (by /u/Pretty_Emu9894)"
            }
    params = {
            "limit": 10
            }
    response = requests.get(link, headers=auth, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
