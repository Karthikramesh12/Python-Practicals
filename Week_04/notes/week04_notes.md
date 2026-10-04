# Week 4 — Lists, Matrices, Sets, Tuples, Dictionaries, and Reading Minds

Source PDFs in this folder: `MIS41110_lecture_week04.pdf` (44 slides), `MIS41110_practical_week04.pdf`.
**No official solutions yet** — this is the practical worked Monday 5 October 2026 (Week 5).
Strike 12:00–13:00 that day: tutorial runs 10:00–12:00 or 15:00–17:00; 13:00–14:30 is questions only.
NOTE: Exercise 6 needs `data/field_notes.txt` and `data/morale_words.txt` from Brightspace — NOT in this folder.

---

## Part A — Lecture notes

### Recap: tracing a while loop (self-check 3)
```python
count = 0
while count < 5:
    count = count + 1
print(count)    # 5
```
Condition checked only at top of each pass. With `<=` it prints 6. Ctrl+C stops infinite loop. `break` leaves a loop from inside.

### §1 Lists
- Mental model: a row of seats; seat number = **index**, starting at 0.
```python
bestsellers = ["latte", "espresso", "muffin", "cappuccino", "tea"]
daily_revenue = [212.40, 305.90, 198.20, 240.00, 260.10]
latte_card = ["latte", "Caffè Latte", 3.20, True]   # mixed types fine
```
- `type()` → `<class 'list'>`; `len(bestsellers)` → 5.
- Indexing: `bestsellers[0]` → latte; `bestsellers[-1]` → tea (from end: -1 … -5).
- Slices (stop not included):
```python
bestsellers[1:3]     # ['espresso', 'muffin']
bestsellers[:2]      # ['latte', 'espresso']
"espresso"[0:3]      # 'esp'
"espresso"[::-1]     # 'osserpse'  (third slot = step)
daily_revenue[2] *= 1.1   # lists are mutable
del bestsellers[1]        # delete by position (later indexes shift left)
bestsellers[7]            # IndexError: list index out of range
```
- Grow/shrink:
```python
order = []
order.append("latte")
order.append("muffin")
last = order.pop()       # removes & returns LAST element
zeros = [0] * 10
"latte" in order         # True (membership)
```
- `while True:` + `break` = same job as a flag variable. In nested loops `break` leaves only innermost.
- Conversions: `list("latte")` → `['l','a','t','t','e']`; `list(range(5))` → `[0,1,2,3,4]`; `"flat white,double shot".split(",")` → `['flat white', 'double shot']`; `"no sugar please".split()` → `['no','sugar','please']`.
- `sys.argv` is a list: `sys.argv[1:]` = all args after program name.
- `"-".join(["tic","tac","toe"])` → `tic-tac-toe` (inverse of split). `enumerate(seasons)` gives index + value:
```python
for i, s in enumerate(seasons):
    print(f"Season {i+1}: {s}")
```

### §2 Lists II
- **In-place mutation trap** (exam regular):
```python
numbers = [1, 2, 3, 4]
for n in numbers:
    n = n * 2
print(numbers)           # [1, 2, 3, 4]  unchanged!
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)           # [2, 4, 6, 8]
```
- **Dot product = order total**:
```python
quantities = [2, 0, 4]
prices = [3.20, 2.50, 2.40]
total = 0.0
for i in range(len(quantities)):
    total += quantities[i] * prices[i]
print(total)    # 16.0
```
- Toolbox: `reverse()`, `sort()` (in place; `["latte", 3.20].sort()` → `TypeError: '<' not supported between 'float' and 'str'`), `insert(0, "vip")`, `remove("ada")` (first match only; missing → `ValueError: x not in list`), safe remove-all `while "ada" in queue: queue.remove("ada")`, `count("bob")`, `[1,2] + [3]`, `tune *= 3`, `sum(list)` (numbers only). Builtins `max() min() sorted()` (sorted returns a new list).

### §3 Comprehensions & matrices
```python
[x for x in range(5)]                               # build     [0,1,2,3,4]
[x * 2 for x in range(5)]                           # transform [0,2,4,6,8]
[x for x in range(5) if x % 2 == 0]                 # FILTER (if at END) [0,2,4]
["even" if x % 2 == 0 else "odd" for x in range(5)] # CHOOSE (if/else at START)
```
- Matrix = list of lists (row first, then column):
```python
sales = [[12,  8, 5],   # Monday     cols: 0=lattes 1=espressos 2=muffins
         [15, 11, 7],   # Tuesday
         [22, 14, 9]]   # Wednesday
sales[1]       # [15, 11, 7]
sales[1][2]    # 7
for row in sales:
    print(*row)
for i in range(len(sales)):
    for j in range(len(sales[i])):
        sales[i][j] += 1
```

### §4 Sets
- "Who is in the room": no duplicates, no order, no index (`regulars[0]` → TypeError).
```python
regulars = {"ada", "grace", "linus"}
vowels = set("aeiou")        # 5 elements
{"aeiou"}                    # ONE element!
regulars.add("ada")          # already there -> nothing
regulars.remove("linus")
"ada" in regulars            # True
```
- Elements must be immutable (str, numbers, tuples; not lists). Set itself mutable.
- **Mutable**: list, dict, set. **Immutable**: int, float, str, bool, tuple. (exam regular)
- Set algebra:
```python
morning = {"ada", "grace", "bob"}
evening = {"grace", "linus"}
morning | evening   # union {'ada','grace','bob','linus'}
morning & evening   # intersection {'grace'}
morning - evening   # difference {'ada','bob'}
morning ^ evening   # exactly one {'ada','bob','linus'}
```
  Print order of a set may vary. Set comprehension: `{w for w in review.split() if w in lexicon}`.

### §5 Tuples
- A ticket: fixed values, in order, can't change.
```python
line = ("latte", 2)
line2 = "muffin", 4       # the COMMA makes the tuple
empty = ()
single = "espresso",      # singleton needs comma
not_a_tuple = ("espresso")   # just a string
line[0]                   # 'latte'
line[1] = 3               # TypeError: no modification
```
- Immutable → usable in sets and as dict keys; faster.
- Unpacking: `b, c = a`; swap `b, c = c, b`; loop `for product, quantity in order:`.
- `sorted(set("abcde"), reverse=True)` works on any iterable.

### §6 Dictionaries
- Name cards on seats: key → value.
```python
prices = {"coffee": 2, "water": 1, "muffin": 3}
prices["muffin"]        # 3
prices["tea"] = 2       # add
prices["tea"] = 2.2     # replace
del prices["water"]
"coffee" in prices      # membership tests KEYS
print("Items:", *prices.keys())
print("Total:", sum(prices.values()))
for product in prices:  # iterates keys
    print(product, prices[product])
```
- Keys: immutable & unique. Values: anything. Keys keep insertion order. `dict(pi=3.14, e=2.72)`; comprehension `{x: x**2 for x in (1, 2, 3)}`.
- Menu becomes data (replaces if/elif `price_of`):
```python
MENU = {"espresso": 2.50, "latte": 3.20, "cappuccino": 3.00,
        "croissant": 2.80, "muffin": 2.40, "tea": 2.20}
```
- Nested dicts: `clients[1]["name"]`; missing key → `KeyError: 0`.
- `.get(key, default)`: `totals[product] = totals.get(product, 0) + score`.

### §7 Case study: sentiment analysis
1. Load lexicon file (`word,weight` lines) into a dict:
```python
DATA_DIR = "data/"

def load_lexicon():
    """Read the sentiment lexicon (word,weight per line) into a dict."""
    lexicon = {}
    for line in open(DATA_DIR + "lexicon.txt"):
        parts = line.strip().split(",")
        lexicon[parts[0]] = float(parts[1])
    return lexicon
```
2. Score each review (after skipping header), accumulate per product (the **counting pattern**):
```python
product, text = line.split(",", 1)     # split ONCE: text may contain commas
score = 0.0
for word in text.lower().split():
    if word in lexicon:
        score = score + lexicon[word]
if product in totals:
    totals[product] = totals[product] + score
    counts[product] = counts[product] + 1
else:
    totals[product] = score
    counts[product] = 1
```
3. Average per product, `round(value, 2)`. Result e.g. latte 1.5, muffin -0.83.
- Limits: bag-of-words misses negation ("not great" scores positive). Validate with labelled data when available. Same skill used in group project's news feed.

### Exam pointers (Week 4)
Predict list operations (indexing/slicing, sort on mixed types, remove of a missing value); rewrite index-loop as comprehension (or back); trace in-place-mutation trap; distinguish list vs set vs tuple vs dict and justify; walk the sentiment loop by hand on three lines.

### Checklist
Build/index/slice lists, mutate in place, know when value-loop doesn't · append/pop/insert/remove/sort/count + their errors (IndexError, TypeError, ValueError) · four comprehension shapes, matrix indexing · choose list/tuple/set/dict · tuple unpacking & swap · set ops `| & - ^` · walk a dict (in, keys(), values()), build by accumulation · text → data with split(), lexicon dict, scoring loop.
Rule of thumb: order → list, fixed shape → tuple, uniqueness → set, lookup → dict.

---

## Part B — Practical sheet, Week 4 (full text)

**Exercise 1: colony counts, listed** — Start from `counts = [242, 60, 120, 80, 182]`.
1. Print first entry, last entry (negative index), middle three (one slice).
2. Append 140.
3. The 60 was a miscount: replace in place with 74 (assign at index).
4. Print total, largest, and a sorted copy (keep original unsorted). Use `max()`, `min()`, `sorted()`.
5. How many times does 242 appear (`count`)? Then `pop()` the last entry and print what came off.

**Exercise 2: tag the species** — Tuples `(species, count)`:
```python
census = [("adelie", 242), ("emperor", 60), ("gentoo", 120), ("chinstrap", 80)]
```
1. Loop and print `adelie: 242` style lines, unpacking each tuple in the for line.
2. Swap two variables `a, b = b, a`; comment what tuples have to do with it.
3. Try `census[0][1] = 250`. Read the error; comment why tuples refuse.

**Exercise 3: who has been out on the ice?**
```python
monday = {"vera", "tom", "ines", "kofi"}
tuesday = {"tom", "kofi", "lena"}
```
Print, each from one set expression: everyone at least once; both days; Monday only; exactly one of the two days.

**Exercise 4: the supply ledger** — `supplies = {"fuel drum": 17, "ration box": 42, "med kit": 9}`.
1. Add `"tea chest"` with count 12.
2. Ten ration boxes go out: update the count.
3. Print all item names, then all counts, then the total (sum over values).
4. Dict comprehension: same items with every count doubled; print it.

**Exercise 5: the census grid** — rows = days (Mon, Tue, Wed), columns = colonies (North Ridge, Seal Point, Windward):
```python
grid = [[242, 182, 210],
        [245, 185, 213],
        [240, 180, 208]]
```
1. Print middle day's counts (one row), and Seal Point's Tuesday count (one value).
2. Each colony's three-day total with a loop over row indexes (column sums).
3. One comprehension: a list of each day's total.

**Exercise 5b ☆: name the smallest colony**
```python
colonies = ["North Ridge", "Seal Point", "Windward"]
counts   = [242, 60, 120]
```
Write `smallest_colony(colonies, counts)` returning the NAME with fewest penguins. Track an index: `best = 0`, `for i in range(len(counts))`, if `counts[i]` beats `counts[best]` remember i; return `colonies[best]`. Should return `'Seal Point'`. Check when smallest is first and when last.

**Exercise 6: the morale scorer (case study)** — `data/field_notes.txt` holds `colony,note` lines (first line header: read off and ignore); `data/morale_words.txt` holds `word,weight` lines. First write the plan as four pseudo-code lines (load lexicon → read notes → score each note → accumulate per colony). Then:
1. Load lexicon into a dict (`split(",")`, float the weight);
2. Read each note (`split(",", 1)`), score by summing weights of known words, accumulate total per colony in a dict;
3. Print one line per colony, rounded to one decimal:
```
North Ridge: 2.4
Seal Point: 3.8
Windward: 1.7
```
(a) The note "generator broken again, crew tired and hungry" scores -1.7. Recompute by hand from the lexicon.
(b) Optional: label five notes good/bad yourself, build a mini lexicon (+1 good words, -1 bad words), score all twenty notes, compare colony ranking.

---

## Part C — Solutions

Not released yet (tutors release after the Monday 5 Oct session). Claude-written solutions to be added later in a separate folder.
