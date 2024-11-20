#difference between primitive data type (int, float, boolean and string)
# complete data type e.g lists of objects, integer ....

#List of names separated by commas
names =["John", "Bob", "Mosh", "Sam", "Mary"]
print(names) #print all the names in the list
print(names[0]) #print the first name in the list from index 0
print(names[-1]) #special features for Python, not found in other languages; -1 is Mary
print(names[-2]) #second element from the back of the list -2 is Sam

#how to change name
names[0] = "Jon"
print(names) #John is changed to Jon in the list
# names[0].replace("Jon","Johnny") # tried this and it didn't work ???
print(names[0:3]) #return names from indesx 0 to 3 excludes last index - (0,1,2) John, Bob and mosh

#List is an object which has methods
numbers = [1,2,3,4,5]
#How to add a new number
numbers.append(6) #APPEND - add another number at the end of the list
print(numbers)
numbers.insert(0,-1) #use command + P to show what the methods expect i.e index & object
print(numbers)
numbers.remove(3) #remove the item on index 3 from the list
print(numbers)
numbers.clear() #CLEAR does not expect any value, rmove all
print(numbers) #Returns empty square brackets
print(1 in numbers) #check if 1 exist in the numbers list and returna a boolean value

numbers = [1,2,3,4,5]
print(len(numbers)) #return the count of items in the list