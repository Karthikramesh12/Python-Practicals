# Week 2, Exercise 4 -- the supply table
# Topics: format specs inside f-strings
#   :<12   left-align in a space 12 characters wide
#   :>9.2f right-align in a space 9 wide, as a float with 2 decimals

item1 = "fuel drum"
weight1 = 180.0
item2 = "ration box"
weight2 = 22.5
item3 = "med kit"
weight3 = 9.75

print(f"{'ITEM':<12} {'WEIGHT KG':>9}")    # text can be formatted too
print(f"{item1:<12} {weight1:>9.2f}")
print(f"{item2:<12} {weight2:>9.2f}")
print(f"{item3:<12} {weight3:>9.2f}")
