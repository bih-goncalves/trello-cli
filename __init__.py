import sys
import trello

options = {
  "boards": {
      "create": trello.default ,
      "ls": trello.default ,
      "delete": trello.default
  },
  "cards": {
      "create": trello.default ,
      "ls": trello.default ,
      "delete": trello.default ,
      "comment": trello.default ,
      "categorize": trello.default
  },
  "labels": {
      "create": trello.default ,
      "ls": trello.getLabels ,
      "delete": trello.default
  },
  "lists": {
      "create": trello.default ,
      "ls": trello.getLists ,
      "delete": trello.default
  }
}

args = sys.argv

# check for first option - entity
if (len(args) > 1) and (args[1] in options.keys()):
    opt1 = options[args[1]]
else:
    print("Sorry, we don't have this option. Instead, try to use: ")
    for key in options:
        print(key + " -- options")
    quit()

# check for second option - method
if (len(args) > 2) and (args[2] in opt1.keys()):
    opt2 = opt1[args[2]]
else:
    print("Sorry, we don't have this option. Instead, try to use: ")
    for key in opt1:
        print(args[1] + " " +key + " -- options")
    quit()

print(opt2(args[3:]))
