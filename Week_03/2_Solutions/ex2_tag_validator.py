# Week 3, Exercise 2 -- the tag validator
# Topics: while loop for input validation (the "muffin rush" pattern)
# (a) while, because we repeat UNTIL the answer is valid and cannot know
#     in advance how many wrong answers will come. for is for a known
#     number of steps.

tag = int(input("Tag number: "))          # ask once BEFORE the loop
while tag < 1 or tag > 500:               # loop while the answer is WRONG
    print("Tags run 1-500. Try again.")
    tag = int(input("Tag number: "))      # ask again INSIDE the loop
print(f"Tag {tag} logged.")               # we only get here with a valid tag
