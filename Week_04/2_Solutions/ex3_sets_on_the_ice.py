# Week 4, Exercise 3 -- who has been out on the ice?
# Topics: sets and the four set operators  |  &  -  ^
# Sets have no order, so the names may print in a different order on your
# machine. That is fine: only the contents matter.

monday = {"vera", "tom", "ines", "kofi"}
tuesday = {"tom", "kofi", "lena"}

print("At least once:  ", monday | tuesday)   # UNION: in either set
print("Both days:      ", monday & tuesday)   # INTERSECTION: in both sets
print("Monday only:    ", monday - tuesday)   # DIFFERENCE: in monday but not tuesday
print("Exactly one day:", monday ^ tuesday)   # SYMMETRIC DIFFERENCE: in one, not both
