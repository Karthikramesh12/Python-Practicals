# Week 3 — Flow Control · Pseudo-code · UML Activity Diagrams

Source PDFs in this folder: `MIS41110_lecture_week03.pdf` (39 slides), `MIS41110_practical_week03.pdf`, `MIS41110_practical_week03_solutions.pdf`.
Still no lists or dicts this week.
NOTE: Exercises 5–6 need `data/field_notes.txt` from Brightspace — NOT in this folder.

---

## Part A — Lecture notes

### Recap: open() gives a bookmark, not the text
- `open()` reads nothing; returns file object = location + bookmark. Each read moves the bookmark.
- `readline()` → one line, bookmark to next line (two calls → two different lines). `read()` → rest of file (next read gives `''`). `tell()` reads bookmark, `seek(n)` moves it.
- `"w"` empties, `"a"` appends, `write()` strings only, nothing on disk until `close()`.
- Self-check Q: `first = log.___()  # exactly one line` → `readline`.

### §1 Think first: pseudo-code → UML activity diagram → code
- Business analytics = decisions. Need **flow control**.
- **Pseudo-code**: numbered plain-English steps. Example even/odd:
  1. Ask user for a number; 2. Compute remainder ÷ 2; if 1 print "odd", if 0 print "even"; 3. Quit.
- **UML activity diagram** symbols (exam uses them):
  - filled black dot = **start**
  - rounded rectangle = **action**
  - diamond = **decision node** (label outgoing edges, e.g. yes/no or Y/N)
  - dot with extra ring (bullseye) = **end**
  - arrows = flow of control
  - (bigger diagrams: multi-way decision node, expand-activity boxes)
- Translate both directions: diagram ↔ English ↔ Python.
```python
number = input("Number? ")
if int(number) % 2 == 1:
    print("Number is odd.")
else:
    print("Number is even.")
```

### §2 Decisions: if / elif / else
```python
if boolean_condition:
    command       # runs only when True
command           # unindented = always runs
```
```python
if total > 20.0:
    print("A feast!")
elif total > 10.0:
    print("A big order.")     # checked in order, first hit wins
else:
    print("A quick coffee.")  # catch-all, no condition
```
- Discount function (named constants, docstring):
```python
DISCOUNT_THRESHOLD = 10.0   # orders over this get a discount
DISCOUNT_RATE = 0.10        # 10% off

def apply_discount(total):
    """Happy-hour rule: a percentage off orders over the threshold."""
    if total > DISCOUNT_THRESHOLD:
        return total * (1.0 - DISCOUNT_RATE)
    else:
        return total
```
  Test boundaries: 9.99 unchanged, 10.00 unchanged (`>` not `>=`), 20.00 → 18.00.
- **Nested ifs** and the **dangling else**: indentation decides which `if` the `else` belongs to.
```python
if hard:                 |  if hard:
    if glitters:         |      if glitters:
        print("gold")    |          print("gold")
    else:                |  else:
        print("useless") |      print("useless")
# else pairs with GLITTERS | else pairs with HARD
```
- Predict exercise (`total = 12.0`, `items = 2`): first block prints A; second prints C; nested block (outer True, inner `items > 3` False, else belongs to outer) prints **nothing**.

### §3 Repetition: while
- Muffin rush: keep asking while answer invalid (nested ifs can't handle a stubborn customer).
```python
stock = 15
asked = int(input("How many muffins? "))
while asked < 1 or asked > stock:
    print(f"You can't buy {asked} muffins.")
    asked = int(input("How many muffins? "))
stock -= asked
```
- Syntax: `while condition:` body repeats while True; then continues after.
- **Sentinel** loop:
```python
nbr = int(input("A number and I'll square it (0 to quit): "))
while nbr != 0:
    print(f"The square is {nbr * nbr}.")
    nbr = int(input("Another one (0 to quit): "))
print("The end.")
```
  Something in the body must be able to change the condition.
- **Menu loop** (shape reused all term):
```python
choice = ""
while choice != "0":
    print("\n[1] New order  [2] Today's revenue  [3] Day summary  [0] Close up")
    choice = input("Choose: ").strip()
    if choice == "1":
        ...            # then elif for 2, 3 and 0: one branch each
    else:
        print("Please choose 1, 2, 3 or 0.")
```
  `.strip()` trims spaces/newlines; `.lower()` lowercases.
- `take_order()`: sentinel while with flag `still_ordering`, running `order_total` and `item_count`, `price_of(product)` (if/elif chain returning 0.0 for unknown), then `apply_discount`.
- **Trace table** (2 latte, 1 muffin, done): order_total 0.00 → 6.40 → 8.80 → return. Tracing a loop line-by-line = exam skill.

### §4 for and iterables
```python
from sys import argv
print("Arguments to this program:", end="")
for arg in argv:
    print(" " + arg, end="")
print()
```
- `for variable in sequence:` once per element. while = until condition flips; for = each element.
- Strings iterate by character:
```python
for letter in "Hello, World!":
    print(letter + "-", end="")      # H-e-l-l-o-,- -W-o-r-l-d-!-
```
- **`in` as membership test**: `"e" in "espresso"` → True. Vowel filter: `if letter in "aeiou":`.
- `for n in 1234:` → `TypeError: 'int' object is not iterable`. Fix: `for n in str(1234):`.
- **range()** — end never included:
```python
range(1, 5)      # 1 2 3 4
range(5)         # 0 1 2 3 4
range(0, 10, 3)  # 0 3 6 9
range(5, 0, -1)  # 5 4 3 2 1
```
- Files are iterable (one line per pass, each with `\n` → `.strip()`):
```python
def day_summary():
    count = 0
    total = 0.0
    for line in open("receipts.txt"):
        line = line.strip()
        if line != "":
            count = count + 1
            total = total + float(line)
    print(f"  Orders today: {count}")
    print(f"  Total revenue: {total:.2f}")
```
- Starred: `print(*range(5))` → `0 1 2 3 4`; `print(*"Hello", sep="-")` → `H-e-l-l-o`.
- Try-it: 10 dashes with for/range; count spaces in "The Daily Grind"; `range(10, 0, -2)` → 10 8 6 4 2.

### §5 How professionals build
- Grow in versions, test after each: v1 broad idea (menu once, if/elif) → v2 persistence (save functions, docstrings) → v3 decisions (discount; test 9.99/10.00/10.01) → v4 menu loop + else for junk.
- Redraw diagram before each version. Diagram → build → test → repeat.
- First-morning crash: `open("revenue.txt")` when file missing → `FileNotFoundError: [Errno 2] No such file or directory`. Real fix = Week 5 exceptions. Today: create receipts.txt fresh at open-up `open("receipts.txt", "w").close()`.
- Pause-per-line: `for line in open("specials.txt"): print(line, end=""); dummy = input(" --ENTER for more--")`.

### §6 Three classic traps
1. `if choice = "1":` → SyntaxError (`=` vs `==`).
2. Boundary: `>` or `>=`? Be consistent.
3. Infinite loop: forgot to re-read `choice` inside loop (Ctrl+C to escape). When a program hangs: can the condition ever change?

### Exam pointers (Week 3)
Draw an activity diagram for a described process (official symbols); hand-trace while/for (table method); find the error (three traps, dangling else); rewrite while as for (or back); state what `range(5, 0, -1)` produces.

### Checklist
Pseudo-code → UML → code (both directions) · if/elif/else, nested ifs, dangling else · while input validation (muffin rush) · menu loop and why one hangs · for over argv/strings/files, 4 range shapes, `in` · small tested versions, docstrings, diagram first.

---

## Part B — Practical sheet, Week 3 (full text)

**Exercise 1: draw before you code** — Draw the UML activity diagram (start/end nodes, action boxes, decision diamonds, labeled edges) for:
```python
crew = int(input("Crew on station: "))
while crew != 0:
    if crew > 40:
        boxes = 3
    elif crew > 20:
        boxes = 2
    else:
        boxes = 1
    print(f"Open {boxes} ration boxes.")
    crew = int(input("Crew on station: "))
```
(a) One sentence: what does the diagram show that the code hides?

**Exercise 2: the tag validator** — Tags numbered 1 to 500. Keep asking `Tag number: ` until in range, then confirm:
```
Tag number: 0
Tags run 1-500. Try again.
Tag number: 612
Tags run 1-500. Try again.
Tag number: 77
Tag 77 logged.
```
(a) Which loop fits and why: while or for?

**Exercise 3: the comms menu** — Build a menu loop:
```
[1] Weather  [2] Colony count  [0] Sign off
Choose: 1
Outside: -17.1 C, wind 35 km/h
[1] Weather  [2] Colony count  [0] Sign off
Choose: 5
Please choose 1, 2 or 0.
[1] Weather  [2] Colony count  [0] Sign off
Choose: 2
North Ridge: 242 adelie penguins at last count.
[1] Weather  [2] Colony count  [0] Sign off
Choose: 0
Farpoint signing off.
```
(Hard-code weather line and count; the loop is the exercise.)

**Exercise 4: for and range() drills**
1. Print countdown `10 9 8 ... 1 LIFT` (for over range with negative step, then one final print).
2. Print a divider of 30 dashes using a loop.
3. Loop over `"Farpoint"` and count lowercase vowels (`if letter in "aeiou"`), print the count.

**Exercise 5: blizzard watch** — `data/field_notes.txt` holds one field note per line (first line header). Put `data/` beside the program and run from that folder. Using `for line in open(...)`, count notes mentioning `blizzard`, print:
```
3 blizzard notes this season.
```
(a) Your loop reads the header too. Does that change this count? When would it?

**Exercise 6 ☆: one colony's file** — Write `colony_extract.py`. Two arguments: notes file and colony name. Writes every note line starting with that colony into `<colony>.txt`, and reports. Wrong number of arguments → usage message and stop (if/else). Given tools: `len(sys.argv)` (3 when two passed), `line.startswith(colony + ",")`.
```
$ python3 colony_extract.py
USAGE: colony_extract.py notes_file colony_name
$ python3 colony_extract.py data/field_notes.txt Windward
6 notes written to Windward.txt.
$ python3 colony_extract.py data/field_notes.txt "North Ridge"
7 notes written to North Ridge.txt.
```
Two-word colonies must be quoted, else they arrive as two arguments → usage message.
Test every branch: happy path, wrong path, boundary.

---

## Part C — Official solutions, Week 3

**Ex 1** — Diagram (described):
start ● → [read crew] → ◇ `crew ≠ 0?` —no→ end ◉
 —yes→ ◇ `crew > 40?` —yes→ [boxes = 3] → [print boxes, then read crew]
  —no→ ◇ `crew > 20?` —yes→ [boxes = 2] → [print boxes, then read crew]
   —no→ [boxes = 1] → [print boxes, then read crew]
[print boxes, then read crew] → back to ◇ `crew ≠ 0?`.
Preview: a `continue` (Week 5) draws as one more edge straight back to the decision diamond.
(a) The diagram shows the **flow**: every path a run can take, and that the loop always returns to the same decision — all at once rather than line by line.

**Ex 2**
```python
# (a) while: we repeat UNTIL a condition holds; we cannot know how many tries.
tag = int(input("Tag number: "))
while tag < 1 or tag > 500:
    print("Tags run 1-500. Try again.")
    tag = int(input("Tag number: "))
print(f"Tag {tag} logged.")
```
(a) while: unknown number of wrong answers. for is for a known number of steps.

**Ex 3**
```python
choice = ""
while choice != "0":
    print("[1] Weather  [2] Colony count  [0] Sign off")
    choice = input("Choose: ")
    if choice == "1":
        print("Outside: -17.1 C, wind 35 km/h")
    elif choice == "2":
        print("North Ridge: 242 adelie penguins at last count.")
    elif choice == "0":
        print("Farpoint signing off.")
    else:
        print("Please choose 1, 2 or 0.")
```

**Ex 4**
```python
for number in range(10, 0, -1):
    print(number, end=" ")
print("LIFT")

for n in range(30):
    print("-", end="")
print()

vowels = 0
for letter in "Farpoint":
    if letter in "aeiou":
        vowels = vowels + 1
print(vowels)
```

**Ex 5**
```python
# (a) The header has no "blizzard", so the count is safe today. It would break the
#     moment a header word matched what we count -- skip headers on principle.
notes = 0
for line in open("data/field_notes.txt"):
    if "blizzard" in line:
        notes = notes + 1
print(f"{notes} blizzard notes this season.")
```

**Ex 6 ☆**
```python
import sys

if len(sys.argv) != 3:
    print("USAGE: colony_extract.py notes_file colony_name")
else:
    notes_file = sys.argv[1]
    colony = sys.argv[2]
    out_file = open(colony + ".txt", "w")
    written = 0
    for line in open(notes_file):
        if line.startswith(colony + ","):
            out_file.write(line)
            written = written + 1
    out_file.close()
    print(f"{written} notes written to {colony}.txt.")
```
