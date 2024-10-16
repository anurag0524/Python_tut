# customer = {
#     "name":"John Smith",
#     "age":30,
#     "is_verified":True
# }

# customer["name"] = "Anurag Samdariya"
# print(customer["name"])
# print(customer.get("birthday","May 24 2002"))

# Exercise 

phone_number = input("Phone Number : ")

digits = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
output = ""
for ch in phone_number:
    output+=digits.get(ch, "!")+" "
print(output)