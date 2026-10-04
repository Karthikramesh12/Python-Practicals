# Week 2, Exercise 1 -- arguments math
# Run from the terminal with two numbers, for example:
#   python ex1_pair_math.py 13 5
#
# (c) sys.argv[0] is the program's own name ("ex1_pair_math.py"), so the
#     first real argument is sys.argv[1] and the second is sys.argv[2].
# (d) We can COMPUTE the "big pair" answer (True/False) this week, but we
#     cannot ACT on it until we learn "if" (Week 3).
import sys

a = float(sys.argv[1])        # arguments arrive as TEXT -> convert to float
b = float(sys.argv[2])

print(f"{a} + {b} = {a + b}")     # f-string: the expression goes inside { }
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")

big_pair = a > 10.0 and b > 10.0  # "and": BOTH must be True
print(f"Big pair (both over 10)? {big_pair}")
