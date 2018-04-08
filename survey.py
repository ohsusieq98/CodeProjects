

name= input ("Please enter your name")  
weightLbs=float(input ("Please enter your weight in lbs")) 
age=int (input("Please enter your age (whole number):")) 
weightKg= weightLbs*0.453592
title= "Human"

print ("Hello", title, name, "your weight is")
print (weightLbs, "lbs")
print ("which equals %.2f" %weightKg,)
print ("kilograms")
