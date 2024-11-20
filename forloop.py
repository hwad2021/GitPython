#FOR LOOP
numbers = [1,2,3,4,5]
for item in numbers: #item is a variable declared in FOR LOOP and iterates through the list
    print(item) #Print each of the item in new line

#WHILE LOPP - alternative way
i = 0
while i < len(numbers):  #Condition is less than the size of the list
    print(numbers[i])
    i = i + 1