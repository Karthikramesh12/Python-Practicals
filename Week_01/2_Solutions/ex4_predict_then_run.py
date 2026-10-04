# Week 1, Exercise 4 -- predict, then run
# Each comment is the prediction, with the reason.

print(2 + 3 * 4)          # 14   (* happens before +)
print((2 + 3) * 4)        # 20   (brackets first)
print(3 * 2 ** 2)         # 12   (** happens first: 2**2 = 4, then 3*4)
print(7 // 2)             # 3    (floor division: whole part only)
print(7 % 2)              # 1    (remainder)
print(True + True)        # 2    (True behaves like 1)
print(str(3) + str(0.5))  # 30.5 <- a STRING: "3" + "0.5" joined   (a)
print(int("13") + 5)      # 18   (text "13" turned into the number 13)
print("13" + str(5))      # 135  <- a STRING: "13" + "5" joined    (a)
