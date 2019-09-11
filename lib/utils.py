#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import logging
import sys

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from config import settings


def build_oauth2_header(logger):
    token = fetch_oauth2_token(logger)
    if token:
        return {
            'Authorization': f"{token.get('token_type')} {token.get('access_token')}" # noqa
        }
    else:
        logger.error('Unable to build authorizatoin header')


def fetch_oauth2_token(logger):
    try:
        client = BackendApplicationClient(client_id=settings.TWITTER_APP_KEY)
        oauth = OAuth2Session(client=client)
        return oauth.fetch_token(
            token_url='https://api.twitter.com/oauth2/token',
            client_id=settings.TWITTER_APP_KEY,
            client_secret=settings.TWITTER_APP_SECRET,
        )
    except Exception as e:
        logger.error(f'Fetching oauth2 token: {e}')
        return None


def setup_logger_stdout(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
