import sys
import trello

options = {
  "boards": {
      "create": trello.default ,
  },
  "cards": {

  },
  "labels": {
      
  },
  "lists": {

  }
}

args = sys.argv

if args[1] in options.keys():
    opt1 = options[args[1]]
else:
    print("Sorry, we don't have this option. Instead, try to use: ")
    for key in options:
        print(key + " -- options")
    quit()

opt2 = opt1[args[2]]



print(trello.getLists('bS7VxUXP'))