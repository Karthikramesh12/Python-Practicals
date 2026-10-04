# Week 4, Exercise 5 -- the census grid
# Topics: matrix = list of lists, grid[row][col], nested loops, list comprehension

# rows    = days     (0 Monday, 1 Tuesday, 2 Wednesday)
# columns = colonies (0 North Ridge, 1 Seal Point, 2 Windward)
grid = [[242, 182, 210],
        [245, 185, 213],
        [240, 180, 208]]
colony_names = ["North Ridge", "Seal Point", "Windward"]

# 1. The middle day's counts (one ROW), and Seal Point on Tuesday (one VALUE)
print("Tuesday:", grid[1])                 # row 1 = Tuesday
print("Seal Point, Tuesday:", grid[1][1])  # row FIRST, then column

# 2. Each colony's three-day total (column sums), looping over row indexes
for col in range(len(colony_names)):
    total = 0
    for row in range(len(grid)):
        total = total + grid[row][col]     # walk DOWN one column
    print(f"{colony_names[col]}: {total}")

# 3. One comprehension: a list of each DAY's total (row sums)
day_totals = [sum(row) for row in grid]
print("Day totals:", day_totals)
