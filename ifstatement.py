# IF statement 
temperature = 25
#single condition
if temperature > 30: # colon is needed
    #character is automatically indented, indicate a block of code
    print("It's hot day") #aspostrophe after 'it' cause confusion, use "" and not ''
    print("Drink plenty of water")
#Indentation is like using curly bracket in C or C++
print("Done") #this code will always get executed as it is not within the indented block of code

#with a second condition
if temperature > 30: # colon is needed
    #character is automatically indented, indicate a block of code
    #Indentation is like using curly bracket in C or C++
    print("It's hot day") #aspostrophe after 'it' cause confusion, use "" and not ''
    print("Drink plenty of water")
elif temperature > 20: #(20,30)
    print ("It's a nice day")
elif temperature > 10: #(10,20)
    print("it's a bit cold")
else:
    print("It's cold") #this code will get executed if none of the above conditions are true
print("Done") #this code will always get executed as it is not within the indented block of code

# Exe 1 - Weight in (K)g or (L)bs: Ask user to input a weight number 
# and then ask if the number is in K or k for kg 
# or L or l for Lbs

weight = input("Please enter a number for your weight :")
unit = input("Enter K or k if the weight is in Kgs or L or l if the weight is in Lbs : ")
print(unit.upper())
if unit.upper() == "K":
    print("if it is K")
    converted = float(weight)/0.45 #need to cast weight into float or int
    print ("Your weight is "+ str(weight)+" Kgs and " + str(converted) + " Lbs")
else:
    converted = float(weight) * 0.45
    print("Your weight is " + weight+" Lbs and "+ str(converted)+ " Kgs")
print("Done")


# Exe 2 - This time use int at the start if input

weight = int(input("Please enter a number for your weight :"))
unit = input("Enter K or k if the weight is in Kgs or L or l if the weight is in Lbs : ")
if unit.upper() == "K":
    converted = weight/0.45 # no need to cast weight into float or int
    print ("Your weight is "+ str(weight)+" Kgs and " + str(converted) + " Lbs")
else:
    converted = weight * 0.45 #no need to cast weight into float and int
    print("Your weight is " + weight+" Lbs and "+ str(converted)+ " Kgs")
print("Done")