# Week 2, Exercise 3 (starred) -- read the roster back
# Run:  python ex3_crew_list.py crew.txt
# (a) ex2_crew_add.py needed "a" (append, keeps what is there).
#     This program needs "r" (read only). "w" would EMPTY the file first!
import sys

filename = sys.argv[1]
crew_file = open(filename, "r")
contents = crew_file.read()          # read() = the whole file as one string
crew_file.close()

print(f"Crew on file '{filename}':")
print(contents, end="")              # the lines already end with \n, so add nothing
