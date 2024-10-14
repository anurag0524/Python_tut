# full_name = input("What is your name? : ")
# fav_color = input("What is your favorite color? : ")
# print(full_name + " likes " + fav_color)

# Type Conversion

# birthYear = input("Whats your birth year: ")
# age = 2024 - int(birthYear)
# print(age)

# Exercise

# weightInPounds = input("Weight in Pounds: ")
# weightInKgs = int(weightInPounds)/2.20462
# print(weightInKgs)

# Strings

# email ='''
# Hi Anurag,

# Here's our first mail to you.

# Regards,
# Support Team
# '''
# print(email)

# name = 'Anurag'
# print(name[-1])
# print(name[1:-1])

# Formatted Strings

# firstName = "Anurag"
# lastName = "Samdariya"
# msg = f"{firstName} [{lastName}] is a coder"
# print(msg)

#String Methods

string = "ANURAG"
sentence = "This is the world we live in."
#length of string (len) is a general purpose function
print(len(string))
#creates a copy of the original string doesnot converts the original string
print(string.lower())
#replace function
print(string.replace("A","H"))
#in function return the boolean value 
print("ANU" in string)
#find function gives the first occurence of the character in string
print(string.find("A"))
#title function used to change the initial character in each word to Uppercase and the subsequent characters to Lowercase and then returns a new string
print(sentence.title())
print(string)
