# String
# Bunch of Characters
name = "likitha"

# String functions
# Python is immutable in nature-they cant be changed.Once created

#capitalize()
#Returns a copy of the string with first character in capital
result = name. capitalize()
print(result)
print(name)
# id-identity of object-Address Ref.
print(id(name))
print(id(result))

#Uppercase
result1 = name. upper()
print(result1)

#Lowercase
result2 = name. lower()
print(result2)
print(id(result2))

#Swapcase
#Returns a copy of the string with uppercase characters converted into lowercase and viceversa
name = "lIkiThA"
print(name.swapcase())

#Title
#Returns a titlecase version of string.
#where words start with an uppercase character and remaining in lowercase.
name = "welcome to python learning"
print(name.title())

# t1 is Ref. or variable names,"krishna" which is stored in memory
t1 = "krishna"
t2 = "likitha"
print(t1.capitalize())
print(t2.upper())


