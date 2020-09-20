import requests
import os

key = os.environ['KEY']
token = os.environ['TOKEN']

# default
def default():
    print('Sorry, we dont have this feature yet')

# list functions

def getLists(board_id):
    if len(board_id) < 1:
        return "Missing param. Please give the board ID"

    url = f"https://api.trello.com/1/boards/{board_id[0]}/lists"

    query = {"key": key, "token": token}

    response = requests.request(
        "GET", url, 
        params=query
        )

    lists = response.json()

    return lists

# label functions

def getLabels(board_id):
    if len(board_id) < 1:
        return "Missing param. Please give the board ID"

    url = f"https://api.trello.com/1/boards/{board_id[0]}/labels"

    query = {"key": key, "token": token}

    response = requests.request(
        "GET", url,
        params=query
        )

    labels = response.json()

    return labels

# card functions

