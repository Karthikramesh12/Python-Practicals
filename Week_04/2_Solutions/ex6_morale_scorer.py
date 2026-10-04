# Week 4, Exercise 6 -- the morale scorer (case study)
# Topics: reading files, split(), a dict as a lexicon, totals per key
#
# NEEDS: a folder called data/ next to this file, holding
#        field_notes.txt and morale_words.txt (both from Brightspace).
#        Run this file FROM the folder that contains data/.
#
# PLAN (pseudo-code, written before the code, as the sheet asks):
#   1. Load the lexicon: each "word,weight" line -> lexicon[word] = weight
#   2. Read the notes file, skipping the header line
#   3. Score each note: add up the weights of the words we know
#   4. Add each note's score to its colony's total, then print the totals

# --- Step 1: load the lexicon into a dict ---
lexicon = {}
for line in open("data/morale_words.txt"):
    parts = line.strip().split(",")        # "tired,-0.6" -> ["tired", "-0.6"]
    lexicon[parts[0]] = float(parts[1])    # the weight arrives as text -> float it

# --- Steps 2 to 4: read the notes, score them, total per colony ---
totals = {}
notes_file = open("data/field_notes.txt")
header = notes_file.readline()             # read the header OFF: the bookmark moves past it
for line in notes_file:                    # so the loop starts at line 2
    colony, note = line.strip().split(",", 1)   # split ONCE: the note may contain commas
    score = 0.0
    for word in note.lower().split():
        if word in lexicon:                # unknown words score nothing
            score = score + lexicon[word]
    if colony in totals:                   # the counting pattern
        totals[colony] = totals[colony] + score
    else:
        totals[colony] = score
notes_file.close()

for colony in totals:
    print(f"{colony}: {round(totals[colony], 1)}")
