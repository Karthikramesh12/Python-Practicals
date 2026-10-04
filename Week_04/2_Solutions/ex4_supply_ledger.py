# Week 4, Exercise 4 -- the supply ledger
# Topics: dictionaries (add, update, keys, values, sum), dict comprehension

supplies = {"fuel drum": 17, "ration box": 42, "med kit": 9}

# 1. A new item arrives: assigning to a NEW key adds it
supplies["tea chest"] = 12

# 2. Ten ration boxes go out: read the old value, subtract, store it back
supplies["ration box"] = supplies["ration box"] - 10

# 3. Names, then counts, then the total
print("Items:", *supplies.keys())      # * unpacks the keys into separate print values
print("Counts:", *supplies.values())
print("Total items on station:", sum(supplies.values()))

# 4. Dict comprehension: same keys, every count doubled
resupply_plan = {item: supplies[item] * 2 for item in supplies}
print("Resupply plan:", resupply_plan)
