#!/usr/bin/python3
"""A python sscript that returns the number
of subscribers of a subreddit passed to it"""

import requests


def number_of_subscribers(subreddit):
    """A function that returns the number of
       Subscribers from subreddit"""
    apiUrl = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    response = requests.get(apiUrl, headers={"user-agent": userAgent})
    if not response:
        return 0
    retValue = response.json().get('data').get('subscribers')
    if retValue:
        return retValue
    else:
        return 0
