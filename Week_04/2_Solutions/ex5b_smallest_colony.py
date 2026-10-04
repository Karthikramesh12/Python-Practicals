# Week 4, Exercise 5b (starred) -- name the smallest colony
# Topics: parallel lists, tracking an INDEX instead of a value, functions

def smallest_colony(colonies, counts):
    """Return the name of the colony with the fewest penguins."""
    best = 0                               # assume position 0 is the smallest so far
    for i in range(len(counts)):
        if counts[i] < counts[best]:       # found a smaller one?
            best = i                       # remember WHERE it is, not what it is
    return colonies[best]                  # same position in the other list = its name


colonies = ["North Ridge", "Seal Point", "Windward"]
counts = [242, 60, 120]
print(smallest_colony(colonies, counts))           # Seal Point

# The two checks the sheet asks for:
print(smallest_colony(colonies, [10, 60, 120]))    # smallest FIRST -> North Ridge
print(smallest_colony(colonies, [242, 60, 5]))     # smallest LAST  -> Windward
