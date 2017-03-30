#!/usr/bin/env python

# imports
from __future__ import print_function
import urllib2
import json

# global vars/constants
site = "https://umbelmania.umbel.com/"
endpoint = "training/"
endpoint = "championship/"
nr_moves_per_game = 1000  # could get this from the return json doc
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


"""
def calculateMove(json_payload):
    json_payload["move"] = "K"
    return json_payload
"""


def calculateMove(json_payload, opponent_map):
    # TODO: this should really be written as a generator so that
    #       these json docs aren't passed around

    # this is hardcoded for now, but could be built
    # dynamically from the webservice
    k_beats = ["A","B","C","D","E"]
    e_beats = ["F","G","H","I","J"]
    j_beats = ["K","A","B","C","D"]

    movenr = nr_moves_per_game - json_payload["gamestate"]["moves_remaining"]
    anticipated_move = opponent_map["opponent_moves"][movenr]

    if anticipated_move in k_beats:
        json_payload["move"] = "K"
    elif anticipated_move in e_beats:
        json_payload["move"] = "E"
    else:
        json_payload["move"] = "J"

    return json_payload


def loadOpponentMoveMap(opponent):
    fp = open(opponent+".moves", mode='r')
    opponent_map = json.load(fp)
    return opponent_map


def main():
    # load opponent move map
    opponent_map = loadOpponentMoveMap("el-rey-muy-dante")

    # initialize game
    json_payload = getTheMotherLoad(initial_payload, site)
    print("game initialized, json:", json.dumps(json_payload, indent=4))

    """
    # make the first move
    json_payload = calculateMove(json_payload)
    json_payload = getTheMotherLoad(json_payload, site)
    print("first move made, json:", json.dumps(json_payload, indent = 4))
    """

    # run through game, iterating over moves, could get this from the return json doc
    for i in range(1, nr_moves_per_game+1):
        json_payload = calculateMove(json_payload, opponent_map)
        json_payload = getTheMotherLoad(json_payload, site)
        print("move", i, "made, payload:", json_payload)

    # exit
    quit()


if __name__ == "__main__":
    main()
