import requests
import os

key = os.environ['KEY']
token = os.environ['TOKEN']

# default
def default(args):
    return 'Sorry, we dont have this feature yet'

###### list functions

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

####### labels functions

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

def addLabels(args):
    if len(args) < 2:
        return "Missing param. Please give the card ID and labelID"

    url = f"https://api.trello.com/1/cards/{args[0]}/idLabels"

    query = {"key": key, "token": token, "value": args[1]}

    response = requests.request(
        "POST", url, 
        params=query
        )

    label = response.json()

    return label




###### comment functions

def addComment(args):
    if len(args) < 2:
        return "Missing param. Please give the card ID and text"

    url = f"https://api.trello.com/1/cards/{args[0]}/actions/comments"

    query = {"key": key, "token": token, 'text': args[1]}

    response = requests.request(
        "POST", url, 
        params=query
        )

    comment = response.json()

    return comment