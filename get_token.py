#!/bin/env python
# coding: utf-8
from __future__ import print_function

import requests
import os

service_id = os.environ['RECAIUS_ID']
service_password = os.environ['RECAIUS_PASSWORD']
payload = {
    'speech_synthesis': {
        'service_id': service_id,
        'password': service_password,
    },
    'expiry_sec': 3600,
}


def get_token():
    r = requests.post('https://api.recaius.jp/auth/v2/tokens', json=payload)
    print(r.json())  # {u'expiry_sec': 3600, u'token': u'xxxxxxxxxxxxxxxxxxxxx'}
    return r.json()['token']


def extend_token(token):
    r = requests.put('https://api.recaius.jp/auth/v2/tokens', json=payload, headers={'X-Token': token})
    print(r.json())  # {u'expiry_sec': 3600, u'token': u'xxxxxxxxxxxxxxxxxxxxx'}


def dispose_token(token):
    requests.delete('https://api.recaius.jp/auth/v2/tokens', headers={'X-Token': token})


def main():
    # ----------------
    t = get_token()
    # ----------------


if __name__ == '__main__':
    main()
