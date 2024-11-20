#String object 
course = "Python for Beginners" 
# Object has method,use the dot
print(course.upper())
#method find a char, index starts from 0
print(course.find("n"))
# it will display the index of the first character in the string
print(course.find("for"))
#Case sensitive and will return -1 if not found
print(course.find("Y"))
#replace method
print(course.replace('for', '4'))
#replace but not found so it will return 0 or the original string
print(course.replace('x','4'))
#Immutable
print(course.find('Python')) # return 0 as index of P is 0
#Equally the code can be written in this way
print('Python' in course) #instead of returning index 0, it will return a boolean value