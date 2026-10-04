# Week 3, Exercise 1 -- draw before you code
# The exercise is to DRAW the UML activity diagram (see 1_Explanations\ex1_draw_before_you_code.txt).
# This is the code from the sheet, so you can run it and follow the diagram.
# Type crew numbers; type 0 to stop.

crew = int(input("Crew on station: "))
while crew != 0:
    if crew > 40:
        boxes = 3
    elif crew > 20:
        boxes = 2
    else:
        boxes = 1
    print(f"Open {boxes} ration boxes.")
    crew = int(input("Crew on station: "))
