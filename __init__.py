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

# check for first option - entity
if args[1] in options.keys():
    opt1 = options[args[1]]
else:
    print("Sorry, we don't have this option. Instead, try to use: ")
    for key in options:
        print(key + " -- options")
    quit()

# check for second option - method
if args[2] in opt1.keys():
    opt2 = opt1[args[2]]
else:
    print("Sorry, we don't have this option. Instead, try to use: ")
    for key in opt1:
        print(args[1] + " " +key + " -- options")
    quit()

opt2()