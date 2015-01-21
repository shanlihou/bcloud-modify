
# Copyright (C) 2013-2014 LiuLang <gsushzhsosgsu@gmail.com>
# Use of this source code is governed by GPLv3 license that can be found
# in http://www.gnu.org/licenses/gpl-3.0.html

'''This module contains some useful functions to handle encoding/decoding

just like escape(), encodeURLComponent()... in javascript.
'''

import base64
import hashlib
import json
from urllib import parse

def md5(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:md5 15')
    return hashlib.md5(text.encode()).hexdigest()

def sha1(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:sha1 18')
    return hashlib.sha1(text.encode()).hexdigest()

def sha224(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:sha224 21')
    return hashlib.sha224(text.encode()).hexdigest()

def sha256(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:sha256 24')
    return hashlib.sha256(text.encode()).hexdigest()

def sha384(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:sha384 27')
    return hashlib.sha384(text.encode()).hexdigest()

def sha512(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:sha512 30')
    return hashlib.sha512(text.encode()).hexdigest()

def base64_encode(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:base64_encode 33')
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:base64_decode 36')
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        return ''

def url_split_param(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:url_split_param 42')
    return text.replace('&', '\n&')

def url_param_plus(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:url_param_plus 45')
    url = parse.urlparse(text)
    output = []
    if len(url.scheme) > 0:
        output.append(url.scheme)
        output.append('://')
    output.append(url.netloc)
    output.append(url.path)
    if len(url.query) > 0:
        output.append('?')
        output.append(url.query.replace(' ', '+'))
    return ''.join(output)

def escape(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:escape 58')
    return parse.quote(text)

def unescape(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:unescape 61')
    return parse.unquote(text)

def encode_uri(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:encode_uri 64')
    return parse.quote(text, safe='~@#$&()*!+=:;,.?/\'')

def decode_uri(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:decode_uri 67')
    return parse.unquote(text)

def encode_uri_component(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:encode_uri_component 70')
    return parse.quote(text, safe='~()*!.\'')

def decode_uri_component(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:decode_uri_component 73')
    return parse.unquote(text)

def json_beautify(text):
    print('/usr/local/lib/python3.4/dist-packages/bcloud/encoder.py:json_beautify 76')
    try:
        return json.dumps(json.loads(text), indent=4)
    except Exception as e:
        return ''
