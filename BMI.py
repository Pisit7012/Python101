a=float(input("Your weight :"))
b=float(input("Your height :"))/100
c=float(a/(b**2))
print("Your BMI :", c)

if c>=0 and c<=18.5:
    print("You are underweight")
elif c>=18.5 and c<=24.9:
    print("Your are normal weight")
elif c>=25 and c<=29.9:
    print("Your are over weight")
elif c>=30 and c<=34.9:
    print("Your are obese")
elif c>=35:
    print("Your are morbidly obese")
else :
    print("Your data is error")