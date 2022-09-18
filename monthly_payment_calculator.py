# calculate monthly payment
def calculate(p: int, months: int, rate: float):
    return round((rate/12) * (1/(1-(1+rate/12)**(-months)))*p)


if calculate(3000000, 60, 0.12) == 66733:
  print("true")
else:
   print("fals")
if calculate(4000000, 120, 0.10) == 52860:
    print("true")
else:
    print("fals")
if calculate(6000000, 120, 0.10)== 79290:
    print("true")
else:
    print("fals")
if calculate(30, 4, 0.10)== 8:
    print("true")
else:
    print("fals")




