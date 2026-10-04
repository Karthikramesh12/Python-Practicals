# Week 1 — Introduction to Programming: Text, Math, Variables & Types

Source PDFs in this folder: `MIS41110_lecture_week01.pdf` (47 slides), `MIS41110_practical_week01.pdf`, `MIS41110_practical_week01_solutions.pdf`.
Course: MIS41110 Programming for Analytics, Romain Claret, UCD 2026. Running lecture example: "The Daily Grind" café register. Practical theme: "Farpoint Station", Antarctica.

---

## Part A — Lecture notes

### Course map (10 weeks)
W1 types/math/strings/variables · W2 input/output/files/functions · W3 decisions & loops · W4 data structures · W5 memory & exceptions · W6 numpy + pandas + group project · W7 classes · W8 functional + GUIs · W9 complexity · W10 testing & exam prep.

### §1–2 Concepts (theory, examinable)
- **Program** = sequence of operations for a computer to execute. Hardware = physical parts; software = instructions.
- Hardware jobs: Input (keyboard, mouse, network), Output (screen, printer), System (CPU, RAM, OS).
- **Binary**: chips carry current (1) or not (0). Boolean logic (George Boole).
- **Machine language** (binary, CPU-specific) → **Assembly** (mnemonics like LDA, JMP, via assembler) → **High-level languages** (human-readable, via compiler/interpreter). Timeline: 1950s FORTRAN, 1960s COBOL/Basic, 1970s C/SQL/Matlab, 1980s C++/Perl, 1990s Python/Java/PHP/JavaScript.
- Python: by Guido van Rossum; Zen of Python ("Readability counts"); "pythonic" = written the way the language wants.

### §3 First program
```python
print("The Daily Grind is open for business.")
```
- `print()` is a **function**. Python is **case sensitive**: `print` ≠ `Print` ≠ `PRINT`.
- String literal: text in `"..."` or `'...'`. Mismatched quotes → `SyntaxError`.
- Three ways to run Python: (1) interpreter `python3` / Windows `python`, prompt `>>>`, quit with `quit()`; (2) from a file `python3 cafe.py`; (3) IDE (VS Code). Slide notation: `$` = terminal, `>>>` = Python shell.
- **Comments**: everything after `#`. Comment *why*, not *what*.

### §4 Under the hood
- Everything is an **object**. `type("x")` → `<class 'str'>`. `help(str)` lists what a string can do.
- A string underneath = a **sequence of character codes** (ASCII): "H"=72, "e"=101 … (exam question: "what is a string underneath?").

### §5 Working with text
- Escapes: `\"` `\'` literal quote, `\n` newline, `\t` tab, `\\` real backslash, `\b` backspace.
- Triple quotes `'''...'''` / `"""..."""`: no escaping needed, line breaks literal.
- String operators: `+` joins, `*` repeats, `len()` measures.
```python
print("The Daily " + "Grind")   # The Daily Grind
print("=" * 34)                 # receipt divider
print(len("The Daily Grind"))   # 15
print("Single", end=""); print(" line.")   # end= changes what print adds (default newline)
```

### §6 Math
- `+ - * / % ** //`. `%` = remainder (even/odd test: `4 % 2` → 0). `**` = power (`2 ** 5` → 32). `^` is NOT power (`2 ^ 5` → 7). `//` = floor division (`3 // 2` → 1).
- `print` takes several values separated by commas.
- Precedence: `2 + 3 * 4` → 14; `(2 + 3) * 4` → 20; `2 - - 1` → 3; `2 - - - 1` → 1; `2 * 2 ** 2 * 2` → 16 (`**` binds tightest); `3 / 2` → 1.5 vs `3 // 2` → 1. When in doubt: brackets.
- `2 / 0` → `ZeroDivisionError: division by zero`.

### §7 Floats and "the wall"
- int + float → float. `type(2 + 5)` → int, `type(2.0 + 5.0)` → float.
- Floats stored in binary (IEEE-754) → approximate. `10 / 3` → `3.3333333333333335`.
- `3.20 * 3` → `9.600000000000001`; `0.1 + 0.1` → `0.2`; `0.1 + 0.1 + 0.1` → `0.30000000000000004`. 1/10 has no exact binary form; errors accumulate (or cancel: `10/3 + 10/3 + 10/3` → `10.0`).
- Exam one-liner: *a tenth has no exact binary form, so floats carry tiny errors that show when you add or multiply.*
- Ints are unbounded (`1000 ** 103` fine). Floats overflow (`1000.0 ** 103` → `OverflowError`) and underflow (`0.1 ** 324` → `0.0`). int = exact & unlimited; float = fast & approximate.

### §8 Booleans
- `True` / `False` (capitalised; `true` → `NameError`). Type `bool`.
- Behave as ints: True = 1, False = 0. `True + True` → 2; `True / False` → `ZeroDivisionError`.
- `bool()` rule: **zero and empty are False; everything else True** — including `bool("False")` → True (non-empty string; exam trick). `bool(0)` F, `bool(0.001)` T, `bool("")` F.

### §9 Variables
- Variable attaches a name to a value. RHS computed first, then name attached. Type detected automatically.
- Naming rules: letters, digits, `_`; not starting with digit; not one of the 35 keywords (`False None True and as assert async await break class continue def del elif else except finally for from global if import in is lambda nonlocal not or pass raise return try while with yield`).
- Good names: `espresso_price`, not `ep`.
- **Rebinding trace**: `x = 1; y = x + 3.14; x = 7; print(y)` → `4.140000000000001` (y computed from x's value at that moment; rebinding doesn't reach back). Old value garbage-collected. `del(x)` → later `print(x)` gives `NameError`.
- Augmented assignment: `revenue += 7.40` (same as `revenue = revenue + 7.40`). Family: `+= -= *= /= **= %= //=`.

### §10 Types & conversions
- Four types: `str`, `int`, `float`, `bool`. Convert with `str() int() float() bool()`.
- `int(x)` builds a NEW object; must assign: `x = int(x)`. `int(3.14)` → 3.
- `"I am " + 100 + " years old."` → `TypeError: can only concatenate str (not "int") to str`. Fix: `str(x)`.

### Café build: cafe_w1.py
```python
cafe_name = "The Daily Grind"
open_sign = True

espresso_price = 2.50
muffin_price = 2.40

espresso_qty = 2
muffin_qty = 1
total = espresso_price * espresso_qty + muffin_price * muffin_qty

print("=" * 34)
print(cafe_name + ": receipt")
print("=" * 34)
print("espresso x " + str(espresso_qty) + "    " + str(espresso_price * espresso_qty))
print("muffin   x " + str(muffin_qty) + "    " + str(muffin_price * muffin_qty))
print("TOTAL: " + str(total))
print("Open: " + str(open_sign))
```
Limits (= future weeks): no 2-decimal formatting (W2), hard-coded order (input W2), float wall, copy-paste per product (W4).

### Exam pointers (Week 1)
- State output of print / arithmetic / conversion snippets (precedence traps, `bool("False")`, string `*` and `+`).
- Explain float imprecision (`0.1 + 0.1 + 0.1`) in one sentence.
- Spot the error: `Print(...)`, mismatched quotes, `"text" + number`, `true`.
- Theory: machine vs assembly vs high-level; what a string is underneath.

### Checklist
Explain program & language levels · run Python 3 ways · print/escapes/comments · `+ - * / % ** //` + precedence · float imprecision · `bool()` and `True == 1` · variables, `type()`, conversions, why `"text" + number` crashes · setup done.

---

## Part B — Practical sheet, Week 1 (full text)

Covers Week 1 lecture (types, math, strings, variables). Worked Monday of Week 2.

**Exercise 0: the setup gate (do this first)**
1. Open a terminal, run `python3` (Windows: `python`). See `>>>`; type `2 + 2`, get 4, leave with `quit()`.
2. In VS Code create `hello_farpoint.py` with one line printing `Farpoint Station: 44 crew, 4 penguin species, 1 very long night.` Run from terminal: `python3 hello_farpoint.py`. Terminal must be in the file's folder (use VS Code Terminal → New Terminal). "can't open file" = wrong folder → `cd` to it.
3. Line below has one bug; paste, run, read error, fix:
```python
print("Radio check: all stations, please respond)
```

**Exercise 1: supply-crate arithmetic**
`a = 17` fuel drums, `b = 5` sledges. Store in variables and print, using them:
```
Value a is <class 'int'>
Value b is <class 'int'>
17 + 5 = 22
17 - 5 = 12
17 * 5 = 85
17 / 5 = 3.4
17 % 5 = 2
17 ** 5 = 1419857
```
(a) Change the stored values; every line must update without touching the prints (keep b nonzero).
(b) One of the six arithmetic lines prints a different *type*. Which, and why?

**Exercise 2: the station door sign**
Using ONE `print()` and one string (escapes allowed):
```
==============================
   FARPOINT STATION
   "South of everywhere"
   Crew: 44   Winter: yes
==============================
```
(a) The `=` lines must come from `"=" * 30`.

**Exercise 3: temperature math**
Readings: -17.1, -17.1, -17.1.
1. Print their sum. Look closely.
2. Comment: why isn't the sum exactly -51.3?
3. Print the average, and `(9 / 5) * (-17.1) + 32` (Fahrenheit). Average comes out clean (errors can cancel).

**Exercise 4: predict, then run** (write prediction as comment first)
```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(3 * 2 ** 2)
print(7 // 2)
print(7 % 2)
print(True + True)
print(str(3) + str(0.5))
print(int("13") + 5)
print("13" + str(5))
```
(a) Which two lines produce a string?

---

## Part C — Official solutions, Week 1

**Ex 0** — bug is a missing closing quote:
```python
print("Radio check: all stations, please respond")
```
Error was `SyntaxError: unterminated string literal` (caret under opening quote). Habit: read the message — it names the problem and the line.

**Ex 1** (no f-strings yet, so `str()` + `+`):
```python
a = 17
b = 5

print("Value a is", type(a))     # commas: print takes several values
print("Value b is", type(b))
print(str(a) + " + " + str(b) + " = " + str(a + b))
print(str(a) + " - " + str(b) + " = " + str(a - b))
print(str(a) + " * " + str(b) + " = " + str(a * b))
print(str(a) + " / " + str(b) + " = " + str(a / b))    # (b) this one: / always gives a float
print(str(a) + " % " + str(b) + " = " + str(a % b))
print(str(a) + " ** " + str(b) + " = " + str(a ** b))
```
(a) Values computed from a and b, so changing two assignments changes all lines.
(b) `17 / 5 = 3.4`: true division always returns float, even when exact; the others stay int.

**Ex 2**
```python
print("=" * 30 + "\n   FARPOINT STATION\n   \"South of everywhere\"\n   Crew: 44   Winter: yes\n" + "=" * 30)
```
(a) `"=" * 30` is string multiplication: same operator, different job because left operand is a string.

**Ex 3**
```python
t1 = -17.1
t2 = -17.1
t3 = -17.1

print(t1 + t2 + t3)
# Not exactly -51.3: floats are stored in binary, and 0.1 (so 17.1 too) has no exact
# binary form, so tiny representation errors add up -- the week-1 wall.
print((t1 + t2 + t3) / 3)
print((9 / 5) * t1 + 32)
```
Sum prints `-51.300000000000004`.

**Ex 4**
```python
print(2 + 3 * 4)          # 14  (* before +)
print((2 + 3) * 4)        # 20  (parentheses first)
print(3 * 2 ** 2)         # 12  (** binds tightest, then *)
print(7 // 2)             # 3
print(7 % 2)              # 1
print(True + True)        # 2   (True behaves as 1)
print(str(3) + str(0.5))  # 30.5  <- a STRING (a)
print(int("13") + 5)      # 18
print("13" + str(5))      # 135   <- a STRING (a)
```
(a) `str(3) + str(0.5)` → `"30.5"` and `"13" + str(5)` → `"135"`: string concatenation that looks numeric — the trap.
