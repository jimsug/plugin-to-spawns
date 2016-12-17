#!/usr/bin/env python3

import requests, sys


try:
    r = requests.get("http://catfacts-api.appspot.com/api/facts?number=1")
    html_text = r.json()['facts'][0]
except:
    html_text = "Unable to get catfacts right now"
    sys.exit(exception(html_text))

sys.stdout.write(html_text)
