#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import requests


while True:
    d = [('TEST_TAG1', random.random() * 100),
         ('TEST_TAG2', random.random() * 100)]
    try:
        r = requests.post("http://localhost:5000/api/set_tag_list", json=d)
        print(r.status_code, r.text.strip())
    except Exception as e:
        print(e)
    time.sleep(5.0)
