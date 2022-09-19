# calculate monthly payment

def calculate(p: int, months: int, rate: float):
 return (rate/12) * (1/(1-(1+rate/12)**(-months)))*p

# a funkció helyességének összevetése

osszeg = calculate(20,10,1)

if osszeg == 3.0255562468897015 :
    print(      )
    print("3.0255562468897015 = ", osszeg ,"tehát helyes a függvény")
else:
    print("3.0255562468897015 nem egyenlő", osszeg ," tehát helytelen a függvény")