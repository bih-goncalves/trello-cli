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

###### card functions

def createCard(args):
    # check if we need label
    if '-l' in args:
        index = args.index('-l')
        args.pop(index) # remove the option
        label = args.pop(index) # get value of label

        # check if the label exist
        labels = getLabels([args[0]])
        l3 = []
        for item in labels:
            l3.append(item['name'])
        
        if label not in l3:
            return "Sorry, this label doesn't exist. Please create before using."
        else:
            label = labels[l3.index(label)]['id']

    #check if we have comment
    if '-c' in args:
        index = args.index('-c')
        args.pop(index) # remove the option
        comment = args.pop(index) # get value of comment

    if len(args) < 4:
        return "Missing param. Please give the board ID, column number, card name and card description"

    # check the list ID
    lists = getLists([args[0]])
    if len(lists) >= int(args[1]):
        list_id = lists[int(args[1])]['id']
    else:
        return "This list doesn't exist. Please create before using."

    url = f"https://api.trello.com/1/cards"

    query = {"name": args[2], "desc": args[3], "idList": list_id, "key": key, "token": token}

    response = requests.request(
        "POST", url,
        params=query
        )

    card_id = response.json()["id"]

    # add label
    if 'label' in locals():
        addLabels([card_id, label])

    # add comment
    if 'comment' in locals():
        addComment([card_id, comment])

    return card_id


###### comment functions

def addComment(args):
    if len(args) < 2:
        return "Missing param. Please give the card ID and comment's text"

    url = f"https://api.trello.com/1/cards/{args[0]}/actions/comments"

    query = {"key": key, "token": token, 'text': args[1]}

    response = requests.request(
        "POST", url, 
        params=query
        )

    comment = response.json()

    return comment