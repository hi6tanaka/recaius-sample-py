#!/bin/env python
# coding: utf-8
from __future__ import print_function

import requests
import os

import token

token = token.get_token()


# -----------------------

def from_plaintext(token, text, info):
    payload = dict(info)
    payload['plain_text'] = text
    r = requests.post('https://api.recaius.jp/tts/v2/plaintext2speechwave', json=payload, headers={'X-Token': token})
    return r.content


data = from_plaintext(token, 'お元気ですか？', {
    'lang': 'ja_JP',
    'speaker_id': 'ja_JP-F0001-H00T',
    # optional
    'speed': 0,
    'pitch': 0,
    'depth': 0,
    'volume': 0,
    # 話者制限あり
    'happy': 0,
    'angry': 0,
    'sad': 0,
    'fear': 0,
    'tender': 0,
    'voiceelements': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'tag_mode': 0,
    'codec': 'audio/x-linear'
})

with open('output.wav', 'wb') as f:
    f.write(data)
