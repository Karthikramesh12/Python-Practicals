# Week 4, Exercise 2 -- tag the species
# Topics: tuples, unpacking in a for loop, swapping, immutability

census = [("adelie", 242), ("emperor", 60), ("gentoo", 120), ("chinstrap", 80)]

# 1. Print "adelie: 242" style lines.
#    Each item in the list is a tuple of two values, so we unpack it into
#    two names right in the for line.
for species, count in census:
    print(f"{species}: {count}")

# 2. Swap two variables in one line
a = 1
b = 2
a, b = b, a
print("a =", a, " b =", b)            # a = 2  b = 1
# Why this works: the right side "b, a" is first packed into a TUPLE (2, 1).
# Then that tuple is UNPACKED into a and b. The comma is what makes a tuple.

# 3. Try to change a value inside a tuple.
#    The next line is commented out because it crashes the program:
# census[0][1] = 250
# The error:  TypeError: 'tuple' object does not support item assignment
# Why: tuples are IMMUTABLE. Once made, they can never change. A census line
# is a fact ("adelie, 242"), and facts should not wobble.
# To "change" it, replace the whole tuple inside the list (lists ARE mutable):
census[0] = ("adelie", 250)
print(census[0])
