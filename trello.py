import requests
import os

key = os.environ['KEY']
token = os.environ['TOKEN']

# default
def default():
    print('Sorry, we dont have this feature yet')

# list functions

def getLists(board_id):
    url = f"https://api.trello.com/1/boards/{board_id}/lists"

    query = {"key": key, "token": token}

    response = requests.request(
        "GET", url, 
        params=query
        )

    lists = response.json()

    return lists

# label functions

# card functions

