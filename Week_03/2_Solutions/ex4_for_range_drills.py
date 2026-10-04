# Week 3, Exercise 4 -- for and range() drills

# 1. Countdown 10 9 8 ... 1 LIFT
for number in range(10, 0, -1):     # start 10, stop BEFORE 0, step -1
    print(number, end=" ")          # end=" " keeps everything on one line
print("LIFT")

# 2. A divider of 30 dashes, using a loop
for n in range(30):                 # range(30) = 0..29 = 30 times
    print("-", end="")
print()                             # finish the line

# 3. Count the lowercase vowels in "Farpoint"
vowels = 0                          # a counter starts at 0
for letter in "Farpoint":           # a string is a sequence of letters
    if letter in "aeiou":
        vowels = vowels + 1
print(vowels)                       # a, o, i -> 3
