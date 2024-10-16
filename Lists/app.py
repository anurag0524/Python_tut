names = ["sara", "josh", "vicotor", "rafa", "mosh"]
names[-2]="kaeren"
print(names[-2])

#Exercise

numbers = [120,1,3,500,6,9]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)     