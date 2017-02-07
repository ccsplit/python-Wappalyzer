#!/usr/bin/env python
"""Script to update the apps.json file.

Update the apps.json file from
[Wappalyzer](https://raw.githubusercontent.com/AliasIO/Wappalyzer).
"""

import codecs
import requests
import json


def update_apps():
    print("Grabbing the updated list from github.com/AliasIO/Wappalyzer")
    url = 'https://raw.githubusercontent.com/AliasIO/Wappalyzer/master/src/apps.json'
    resp = requests.get(url)
    if resp.ok:
        with codecs.open('data/apps.json', 'w', encoding='UTF-8') as outfile:
            jobject = json.loads(resp.content)
            outfile.write(json.dumps(jobject, indent=2, 
                          separators=(',', ': ')))
        print("Finished updating data/apps.json")
    else:
        print("Unable to connect to {}, reason: {}", url, resp.reason)

if __name__ == '__main__':
    update_apps()
