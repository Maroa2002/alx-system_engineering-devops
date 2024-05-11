#!/usr/bin/python3
'''Module that queries the Reddit API '''
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    '''
    Returns a list containing the titles of all hot articles for
    a given subreddit
    '''
    if after is None:
        return hot_list
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    headers = {'User-Agent': 'VICTORY'}
    response = get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return None
    else:
        rqd_info = response.json()
        ''' Grab list of hot posts '''
        rqd_list = rqd_info.get('data').get('children')
        for list_dict in rqd_list:
            hot_list.append(list_dict['data']['title'])
        return (recurse(subreddit, hot_list, rqd_info['data']['after']))
