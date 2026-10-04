# Week 4, Exercise 1 -- colony counts, listed
# Topics: list indexing, negative index, slicing, append, replace in place,
#         sum / max / sorted, count, pop

counts = [242, 60, 120, 80, 182]      # five census entries

# 1. First entry, last entry (negative index), middle three (one slice)
print("First:", counts[0])            # index 0 = the first item
print("Last:", counts[-1])            # index -1 = the last item, however long the list is
print("Middle three:", counts[1:4])   # items 1, 2, 3 (a slice STOPS BEFORE the end number)

# 2. A sixth census arrives
counts.append(140)                    # append() adds to the END
print("After append:", counts)

# 3. The 60 was a miscount: replace it IN PLACE with 74
counts[1] = 74                        # assign at the index: same list, one item changed
print("After fix:", counts)

# 4. Total, largest, and a sorted COPY (the original stays unsorted)
print("Total:", sum(counts))
print("Largest:", max(counts))
print("Sorted copy:", sorted(counts))  # sorted() builds a NEW list
print("Original still:", counts)       # order unchanged

# 5. How many times does 242 appear? Then pop the last entry
print("242 appears", counts.count(242), "time(s)")
removed = counts.pop()                 # pop() removes the LAST item and hands it back
print("Popped off:", removed)
print("List now:", counts)
