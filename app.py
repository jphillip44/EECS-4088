#!/usr/bin/python3

import sys
import json
import requests

def main():
    conv = {
        'input': {
            'topic1':'Hi',
            'topic2':'Greeting'
        }
    }

    s = json.dumps(conv)
    res = requests.post("http://127.0.0.1:5000/cl/", json=s).json()
    print(res['escalate'])

if __name__ == '__main__':
    main()