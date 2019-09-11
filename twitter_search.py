#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import os

import requests

from lib import utils


search_url = 'https://api.twitter.com/1.1/search/tweets.json'


def search_twitter(logger):
    headers = utils.build_oauth2_header(logger)
    search_params = {
        'q': 'Bahamas',
        'result_type': 'recent',
        'lang': 'en',
        'count': 10,
        'tweet_mode': 'extended',
    }
    results = requests.get(search_url, headers=headers, params=search_params)
    print(results.json)


if __name__ == '__main__':
    # move to working directory...
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    logger = utils.setup_logger_stdout('search_twitter')

    search_twitter(logger)
