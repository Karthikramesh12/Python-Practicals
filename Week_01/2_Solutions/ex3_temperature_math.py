# Week 1, Exercise 3 -- temperature math

t1 = -17.1
t2 = -17.1
t3 = -17.1

print(t1 + t2 + t3)              # -51.300000000000004  (not -51.3!)
# Not exactly -51.3: floats are stored in binary, and 0.1 (so 17.1 too) has no
# exact binary form, so tiny representation errors add up -- the "float wall".

print((t1 + t2 + t3) / 3)        # -17.1  (the errors cancel out here)
print((9 / 5) * t1 + 32)         # the reading in Fahrenheit
