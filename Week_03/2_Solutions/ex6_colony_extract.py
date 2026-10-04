# Week 3, Exercise 6 (starred) -- one colony's file
# Run from the terminal, for example:
#   python ex6_colony_extract.py data/field_notes.txt Windward
#   python ex6_colony_extract.py data/field_notes.txt "North Ridge"
import sys

if len(sys.argv) != 3:                      # program name + 2 arguments = 3
    print("USAGE: colony_extract.py notes_file colony_name")
else:
    notes_file = sys.argv[1]
    colony = sys.argv[2]
    out_file = open(colony + ".txt", "w")   # "w" = a fresh output file
    written = 0
    for line in open(notes_file):
        if line.startswith(colony + ","):   # the comma stops "North" matching "North Ridge"
            out_file.write(line)            # the line already ends with \n
            written = written + 1
    out_file.close()
    print(f"{written} notes written to {colony}.txt.")
