#!/usr/bin/env python

# imports
from __future__ import print_function
import urllib2
import json
import sys

# global vars/constants
site = "https://umbelmania.umbel.com/"
endpoint = "training/"
site = site + endpoint
initial_payload = {}
initial_payload["opponent"] = "el-rey-muy-dante"
initial_payload["player_name"] = "Bodds by Dodds"
initial_payload["email"] = "todd.jones@gmail.com"
print("### START ###")
print("site:", site)
print("initial_payload: ", json.dumps(initial_payload, indent = 4))


def getTheMotherLoad(json_payload, site):
    post = urllib2.Request(site)
    post.add_header('Content-Type', 'application/json')
    return_payload = urllib2.urlopen(post, json.dumps(json_payload))
    if return_payload.msg != "OK":
        print("error retrieving motherload using site [%s] json [%s]") % (site, json)
        quit(1)
    payload_string = ""
    for line in return_payload.readlines():
        payload_string = payload_string + line
    motherload = json.loads(payload_string)
    return motherload


def calculateMove(json_payload):
    json_payload["move"] = sys.argv[1]
    return json_payload


def main():
    # initialize game
    json_payload = getTheMotherLoad(initial_payload, site)
    print("game initialized, json:", json.dumps(json_payload, indent=4))

    """
    # make the first move
    json_payload = calculateMove(json_payload)
    json_payload = getTheMotherLoad(json_payload, site)
    print("first move made, json:", json.dumps(json_payload, indent = 4))
    """

    # make 1000 moves
    for i in range(1, 1001):
        json_payload = calculateMove(json_payload)
        json_payload = getTheMotherLoad(json_payload, site)
        print("move", i, "made, payload:", json_payload)


    # exit
    quit()


if __name__ == "__main__":
    main()


