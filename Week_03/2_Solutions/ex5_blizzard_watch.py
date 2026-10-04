# Week 3, Exercise 5 -- blizzard watch
# NEEDS: data\field_notes.txt from Brightspace, in a "data" folder next to this file.
#
# (a) The header line has no "blizzard" in it, so the count is safe today.
#     It would break the moment a header contained the word being searched
#     for -- so skipping the header on purpose is the good habit.

notes = 0
for line in open("data/field_notes.txt"):   # a file is a sequence of lines
    if "blizzard" in line:                  # "in" tests: is this text inside that?
        notes = notes + 1
print(f"{notes} blizzard notes this season.")
