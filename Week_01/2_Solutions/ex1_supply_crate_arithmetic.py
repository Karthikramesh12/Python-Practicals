# Week 1, Exercise 1 -- supply-crate arithmetic
# No f-strings yet (they arrive in Week 2), so numbers are glued into text
# with str() and +.

a = 17
b = 5

print("Value a is",  type(a))     # commas: print takes several values, adds spaces
print("Value b is", type(b))
print(str(a) + " + " + str(b) + " = " + str(a + b))
print(str(a) + " - " + str(b) + " = " + str(a - b))
print(str(a) + " * " + str(b) + " = " + str(a * b))
print(str(a) + " / " + str(b) + " = " + str(a / b))    # (b) THIS one: / always gives a float
print(str(a) + " % " + str(b) + " = " + str(a % b))
print(str(a) + " ** " + str(b) + " = " + str(a ** b))

# (a) Change a and b above and run again: every line updates, because every
#     printed value is CALCULATED from a and b, not typed in.
# (b) 17 / 5 = 3.4 is a float. True division "/" ALWAYS returns a float,
#     even for 10 / 5 (which gives 2.0). The other lines stay int.
