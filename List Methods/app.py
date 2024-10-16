numbers = [1,2,3,4,5,6]

numbers.append(7)
numbers.insert(6,8) # takes two parameters 1st is the index and 2nd is the value
numbers.remove(2)
numbers.pop()
print(numbers.index(8)) # gives the index of the first appearence of the character on the list  
print(50 in numbers) # gives the boolean value that the given number or character exists in the list or not
print(numbers.count(8)) # returns the number of occurences of the given element on the list
numbers.sort() # doesnt return any value just sorts the list
numbers.reverse() # reverses the list
numbers_1 = numbers.copy() # copies the original list 
numbers.append(40)
print(numbers_1)
print(numbers)

# Excercise to remove  duplicates in a list

numbers = [1,2,3,45,67,3,2,1,3,2]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
    
print(uniques)        