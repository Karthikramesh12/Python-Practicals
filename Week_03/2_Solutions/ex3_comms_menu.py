# Week 3, Exercise 3 -- the comms menu
# Topics: the menu loop -- a sentinel while outside, if/elif/else inside

choice = ""                                # start with anything that is not "0"
while choice != "0":                       # "0" is the sentinel that means stop
    print("[1] Weather  [2] Colony count  [0] Sign off")
    choice = input("Choose: ")             # input() gives TEXT, so compare with "1", not 1
    if choice == "1":
        print("Outside: -17.1 C, wind 35 km/h")
    elif choice == "2":
        print("North Ridge: 242 adelie penguins at last count.")
    elif choice == "0":
        print("Farpoint signing off.")
    else:                                  # anything else is junk input
        print("Please choose 1, 2 or 0.")
