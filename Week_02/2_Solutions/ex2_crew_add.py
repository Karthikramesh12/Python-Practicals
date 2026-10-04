# Week 2, Exercise 2 -- sign the crew in
# Run:  python ex2_crew_add.py crew.txt
# Each run adds ONE line to the file (run it twice to add two crew members).
import sys

filename = sys.argv[1]               # the file name comes from the terminal
name = input("Name: ")
role = input("Role: ")

crew_file = open(filename, "a")      # "a" = append: add to the end, never wipe
crew_file.write(name + " " + role + "\n")   # write() needs text; \n ends the line
crew_file.close()                    # always close what you open
