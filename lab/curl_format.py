# -*- coding: utf-8 -*-
# pylint: disable=broad-except

"""curl to requests
"""

__authors__ = ['"sue.chain" <sue.chian@gmail.com>']

import requests


def curl():
    with open("curl.txt", "rb") as fd:
        curl = fd.readline()
    curl_list = curl.replace("\"", "").replace("--compressed", "").split("-H")
    curl_list.reverse()
    url = curl_list.pop().strip().split(" ")[-1]
    headers = {}
    for item in curl_list:
        print item 
        key, val = item.strip().split(": ")
        headers[key] = val.strip()

    response = requests.get(url, headers=headers)
    print response.json()

def curl_to_code():
    with open("curl.txt", "rb") as fd:
        curl = fd.readline()
    curl_list = curl.replace("\"", "").replace("--compressed", "").split("-H")
    curl_list.reverse()
    url = curl_list.pop().strip().split(" ")[-1]
    headers = []
    for item in curl_list:
        key, val = item.strip().split(": ")
        headers.append("headers[\"{}\"]=\"{}\"".format(key, val.strip()))

    print "\r\n".join(headers)
    print url
    #response = requests.get(url, headers=headers)
    #print response.json()






if __name__ == '__main__':
    print curl_to_code()


