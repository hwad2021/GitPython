#RANGE function

numbers = range(5) #range is from 0 to 5 excluding 5
print(numbers) #returns (0,5) and not the aactual numbers

#using FOR LOOP to iterate
for number in numbers:
    print(number) #return 0,1,2,3,4

# using two values
numbers = range(5, 10)
for number in numbers:
    print(number) #return 5,6,7,8,9

# using three values, third value is to jump values
numbers = range(5, 10, 2) #skip two
for number in numbers:
    print(number) #return 5,,7,9

# range function can be used directly in FOR LOOP
#numbers = range(5, 10, 2) #skip two
print("*")
for number in range(5):
    print(number) #return 0,1,2,3,4