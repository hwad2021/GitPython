# prompt for a birth year and store it in a cariable called birth_year
birth_year = input("Enter your birth year") 
#Integer casting is needed for birth_year as it was in string format
age = 2020 -  int(birth_year)
print(age)

#built in functions for type casting
#int() - convert a value to integer
#float() - number with decimal point
#bool()  - convert a value to a boolean
#str() - convert a value to a string

#Exe1 - basic calculator, ned to enter two value
first = input("Enter a first number ")
second = input("Enter a second number ")
# variable need int() in order to perform mathematic 
#sum = int(first) + int(second)
# float is to show if decimal value is used
floatsum = float(first) + float(second)
print( "The total of the two number is " + str(sum))
print("The total in float format is " + str(floatsum)) 

#Equally use type cast as 'float(input("Enter a first number"))