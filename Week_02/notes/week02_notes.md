# Week 2 — Input & Output · Boolean Logic, Functions, Modules, Scope

Source PDFs in this folder: `MIS41110_lecture_week02.pdf` (44 slides), `MIS41110_practical_week02.pdf`, `MIS41110_practical_week02_solutions.pdf`.
Rule this week: no `if`, no loops — programs run straight top to bottom.

---

## Part A — Lecture notes

### Why 0.1 + 0.1 + 0.1 ≠ 0.3 (recap, examinable)
- A tenth never ends in binary; a float keeps 53 significant bits and rounds the last one.
- `0.1 + 0.1` → `0.2` (doubling just moves the point; no new error). `0.1 + 0.1 + 0.1` → `0.30000000000000004` (adding different sizes needs one more bit; rounds up).
- Python prints the shortest decimal naming the stored value. `0.1 * 3` → 0.30000000000000004 but `0.1 * 4` → 0.4. Never depend on last digits.
- Display fix: format specs (below). Rounding values: Week 4.

### §1 Output: three ways to print + format specs
Programs: data in (keyboard, files, program arguments) → data out (screen, files…).
```python
latte_price = 3.20
lattes = 3
print("Total:", latte_price * lattes)            # commas: mixed types, auto-spaces
print("Total: " + str(latte_price * lattes))     # convert + concatenate (Week 1)
print(f"Total: {latte_price * lattes}")          # f-string: expression in braces
print(f"Total: {latte_price * lattes:.2f}")      # Total: 9.60   <- the fix
```
- **f-string**: prefix `f`, any expression inside `{}`. Evaluated **when the string is created**.
- **str.format()** (older, must read it):
```python
print("There are {} people in this {} now.".format(71, "room"))
print("Order: {0} {1} {2}".format(1, 2.0, "3"))   # by position -> Order: 1 2.0 3
print("Chaos: {2} {0} {1}".format(1, 2.0, "3"))   # any order   -> Chaos: 3 1 2.0
print("{:d} = {:f} = {:e}".format(3, 3, 3))       # 3 = 3.000000 = 3.000000e+00
print("{s} = {n}".format(n=3, s="three"))         # named placeholders
```
  Type codes: `d` int, `f` float decimal, `e` exponential, `s` string.
- **Format specs** (width, precision, alignment, fill):
```python
print(f"{'The Daily Grind':=^34}")             # centred in 34, filled with =
print(f"{'latte':<12} x {3:>2} {9.6:>8.2f}")    # latte        x  3     9.60
```
  `:<12` left-align width 12 · `:>2` right-align width 2 · `:>8.2f` right, width 8, 2 decimals · `:=^34` centre, fill `=`.
  Also `"|{0:-^12}|".format("Center")`, fill char as argument `"|{0:{1}<12}|".format("Left", "-")`.
- Trap: `x = 23; phrase = f"I am {x}"; x = 24; print(phrase)` → still "I am 23" (built at creation).

### §2 Input
```python
name = input("Your name: ")
print(f"Hello, {name}!")
```
- `input()` prints prompt, waits, **always returns a str**.
- Trap: `year = input(...)`; `2026 - year` → `TypeError: unsupported operand type(s) for -: 'int' and 'str'`. Fix: convert immediately: `qty = int(input("How many? "))`.

### §3 Files
- Everything on disk is a file. stdin (keyboard), stdout (screen), stderr. Extensions hint content (.txt, .csv, .py, .xlsx). Text files = character codes (UTF-8).
- `open(name, mode)` returns a **file object** (pointer + bookmark), not the contents.

| Mode | Meaning | After writing twice |
|---|---|---|
| `"r"` | read (default) | n/a |
| `"w"` | write: starts file fresh (**overwrites**) | only line 2 |
| `"a"` | append: adds to end | line 1, line 2 |
| `"r+"` | read and write | — |

```python
menu = open("menu.txt")
print(menu.readline())   # line 1
print(menu.readline())   # line 2: the object REMEMBERS where you are
print(menu.read(21))     # exactly 21 characters
whole = menu.read()      # everything from here to the end
menu.close()
menu.readline()          # ValueError: I/O operation on closed file.
```
- `tell()` reads the bookmark position, `seek(n)` moves it.
- Writing:
```python
revenue_file = open("revenue.txt", "w")   # fresh each close
revenue_file.write(f"{total:.2f}")        # write() wants a string
revenue_file.close()

log = open("receipts.txt", "a")           # running log
log.write(f"{total:.2f}\n")
log.close()
```
- `write(3.14)` → `TypeError: write() argument must be str, not float`. Nothing guaranteed on disk until `close()`.
- Variable dies with program; file survives. Reading a maybe-missing file safely = Week 5 exceptions.

### §4 Program arguments
```python
import sys
cashier = sys.argv[1]               # argv[0] is the program's own name
starting_cash = float(sys.argv[2])  # arguments arrive as strings -> convert
print(f"Register open. {cashier} starts the day with {starting_cash:.2f} in the drawer.")
```
`$ python3 w02_argv_start.py Ada 40.0` → argv[0]=`w02_argv_start.py`, argv[1]=`Ada`, argv[2]=`40.0`.
Import styles: `import sys` → `sys.argv` (pythonic, traceable) vs `from sys import argv` → `argv`.

### §5 Boolean logic
- Comparisons produce `bool`: `< <= > >= == !=`. `hit_target = revenue > target`.
- Strings compare with `==`/`!=`.
- **`=` assigns, `==` compares.** `comparison = product1 = product2` is an assignment chain, not a question.
- `and` (all true), `or` (at least one), `not` (flip).
- **Precedence trap**: priority `not` > `and` > `or`.
  `uni == "UCD" or uni == "DCU" or uni == "TCD" and age > 21` → True for 18-year-old at UCD (age check guards only TCD). Fix with parentheses: `(… or … or …) and age > 21`.
- Truth tables: and = all true; or = at least one; not = invert.
- Register can **compute** a decision (`big_order = total > 10.0`) but can't **act** on it until `if` (W3).

### §6 Functions
```python
def line_total(price, quantity):
    return price * quantity
```
- `def` + name + `(parameters)` + `:` + indented body (4 spaces). `return` hands a value back.
- Zero or more in, zero or more out:
```python
def hello():                 # no inputs, no return
    print("Hello!")

def cube(nbr):               # one in, one out
    return nbr * nbr * nbr

def euros_and_cents(amount): # one in, TWO out
    whole = amount // 1.0
    return whole, amount - whole

euros, cents = euros_and_cents(17.50)   # euros=17.0, cents=0.5
```
- Café refactor:
```python
def receipt_line(product, price, quantity):
    """One aligned receipt row -- the format specs do the layout work."""
    return f"{product:<12} x {quantity:>2} {line_total(price, quantity):>8.2f}"
```
- **Trace table** of `print(receipt_line("latte", 3.20, 3))`: print needs receipt_line first → receipt_line gets product/price/quantity → calls line_total → returns 9.6… → formatted `:>8.2f` → "    9.60" → print shows row. ("State the output" exam questions = this table.)

### §7 Scope
```python
def hello():
    msg = "Hello, world!"   # LOCAL: born in the function, dies with it
    print(msg)

hello()
print(msg)                  # NameError: name 'msg' is not defined
```
- Local variables exist only inside the function. Globals (file level, defined before the call) are readable inside functions; a local of the same name shadows it; assigning inside creates a new local (doesn't change global). `global` keyword forces it — avoid.
- Design rule: functions **receive** what they need and **return** what they produce (`total = line_total(price, qty)`). Don't make `revenue` global.

### §8 Modules
- Built-in: `sys`, `os`, `math`, `random`, `datetime`. `import math; math.sqrt(2)`.
- Own module = just a .py file; import by filename without `.py`. Module executes on import → should hold declarations, not surprise prints.
```python
# register_sayings.py
def welcome(name):
    return f"Welcome to The Daily Grind, {name}!"

goodbye = "Thank you, come again!"

# cafe_w2.py
import register_sayings
print(register_sayings.welcome(cashier))   # module.function()
print(register_sayings.goodbye)            # module.variable
```

### Exam pointers (Week 2)
Output of format specs (`{x:>8.2f}`) and function calls (trace table); input()-returns-string TypeError; `=` vs `==`; and/or precedence trap; local vs global scope; complete a one-line function; pick file mode (`w` vs `a`); unpack two return values; import own module.

### Checklist
Format money (f-strings, .format, width/precision) · input() + convert immediately · open/readline/read/write/close + modes r/w/a · sys.argv and argv[0] · boolean expressions with parentheses · functions with (multiple) returns · local vs global, avoid globals · two-file program with own module.

---

## Part B — Practical sheet, Week 2 (full text)

**Exercise 1: arguments math** — Write `pair_math.py`: reads two decimal values as program arguments; for `python3 pair_math.py 13 5` prints:
```
13.0 + 5.0 = 18.0
13.0 - 5.0 = 8.0
13.0 * 5.0 = 65.0
13.0 / 5.0 = 2.6
13.0 ** 5.0 = 371293.0
Big pair (both over 10)? False
```
(a) Run with different arguments, check correct. (b) Use f-strings. (c) Comment: what is `sys.argv[0]`, why read [1] and [2]? (d) Last line: both values over 10, one printed boolean (`and`). Compute it; can't act until `if`.

**Exercise 2: sign the crew in** — Write `crew_add.py`: each run asks name and role with `input()`, **appends** one line to a file whose name is a program argument.
```
$ python3 crew_add.py crew.txt
Name: Vera Lindqvist
Role: glaciologist
$ python3 crew_add.py crew.txt
Name: Tom Ekwueme
Role: cook
```

**Exercise 3 ☆: read the roster back** — Write `crew_list.py`: same filename argument, prints contents under a header:
```
$ python3 crew_list.py crew.txt
Crew on file 'crew.txt':
Vera Lindqvist glaciologist
Tom Ekwueme cook
```
Hint: `end=` decides what print adds; file lines already carry newlines.
(a) Which `open()` mode did each program need, and why?

**Exercise 4: the supply table** — Write `supply_table.py`: three supplies + weights in six variables, aligned table with `:<12`, `:>9.2f`, one literal space between fields:
```
ITEM         WEIGHT KG
fuel drum       180.00
ration box       22.50
med kit           9.75
```

**Exercise 5: the station math module** — Module `station_math.py` with:
- `c_to_f(celsius)`: returns Fahrenheit;
- `wind_chill(temp_c, wind_kmh)`: `13.12 + 0.6215*t - 11.37*v**0.16 + 0.3965*t*v**0.16`;
- `split_shift(hours)`: returns two values: `hours // 4` full watches, `hours % 4` leftover;
- `is_freezing(celsius)`: returns boolean, True below zero (no `if`).

Then `tonight.py` imports the module and prints (hardcoded -17.1 °C, 35.0 km/h, 11 duty hours):
```
Outside: -17.1 C = 1.22 F
Freezing: True
Feels like: -29.6 C in the wind
Watches: 2 full, 3 hours spare
```
(a) Why does tonight.py stay correct if you improve a formula inside station_math.py?
(b) Scope check in a comment: can tonight.py read a variable created inside wind_chill? Why not?

---

## Part C — Official solutions, Week 2

**Ex 1**
```python
# (c) sys.argv[0] is the program's own name; the real arguments start at [1].
# (d) The program can COMPUTE a decision this week and cannot ACT on it: that
#     needs if, which arrives on Friday.
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")

big_pair = a > 10.0 and b > 10.0
print(f"Big pair (both over 10)? {big_pair}")
```
(a) Nothing hard-coded. (b) f-strings replace str() gluing. (c) argv[0] = program name. (d) 13 clears 10, 5 doesn't; `and` needs both → False.

**Ex 2**
```python
import sys

filename = sys.argv[1]
name = input("Name: ")
role = input("Role: ")

crew_file = open(filename, "a")          # "a": add to the end, never wipe
crew_file.write(name + " " + role + "\n")
crew_file.close()
```

**Ex 3**
```python
# (a) ex2 needed "a" (append across runs); here "r" (read only).
import sys

filename = sys.argv[1]
crew_file = open(filename, "r")
contents = crew_file.read()
crew_file.close()

print(f"Crew on file '{filename}':")
print(contents, end="")                  # lines already carry their own \n
```
(a) crew_add needs "a" (keeps existing). crew_list needs "r". "w" would empty the file first.

**Ex 4**
```python
item1 = "fuel drum"
weight1 = 180.0
item2 = "ration box"
weight2 = 22.5
item3 = "med kit"
weight3 = 9.75

print(f"{'ITEM':<12} {'WEIGHT KG':>9}")
print(f"{item1:<12} {weight1:>9.2f}")
print(f"{item2:<12} {weight2:>9.2f}")
print(f"{item3:<12} {weight3:>9.2f}")
```

**Ex 5** — `station_math.py`:
```python
def c_to_f(celsius):
    """Celsius to Fahrenheit."""
    return (9 / 5) * celsius + 32


def wind_chill(temp_c, wind_kmh):
    """The standard wind-chill formula (temperature in C, wind in km/h)."""
    return 13.12 + 0.6215 * temp_c - 11.37 * wind_kmh ** 0.16 + 0.3965 * temp_c * wind_kmh ** 0.16


def split_shift(hours):
    """Return full 4-hour watches and the leftover hours -- two values."""
    return hours // 4, hours % 4


def is_freezing(celsius):
    """True below zero -- the comparison already IS the boolean."""
    return celsius < 0
```
`tonight.py`:
```python
# (a) tonight.py only calls the functions; better internals change nothing here.
# (b) No: variables born inside wind_chill are LOCAL and vanish when it returns.
import station_math

outside = -17.1
wind = 35.0
duty_hours = 11

watches, spare = station_math.split_shift(duty_hours)

print(f"Outside: {outside} C = {station_math.c_to_f(outside):.2f} F")
print(f"Freezing: {station_math.is_freezing(outside)}")
print(f"Feels like: {station_math.wind_chill(outside, wind):.1f} C in the wind")
print(f"Watches: {watches} full, {spare} hours spare")
```
(a) Caller only uses function names; internals can change — the point of a module.
(b) No: locals exist only while the function runs; only the returned value crosses back.
