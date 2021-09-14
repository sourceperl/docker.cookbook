#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import random
import time


while True:
    try:
        r = requests.get("http://localhost:5000/api/set_tag/TEST_TAG?value=%.2f" % (10 * random.random()))
        print(r.status_code, r.text.strip())
    except Exception as e:
        print(e)
    time.sleep(5.0)
