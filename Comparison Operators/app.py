# temperature = 2

# if temperature >= 30:
#     print("It's a hot day.")
# elif temperature <= 10:
#     print("It's a cold day.")
# else:
#     print("It's neither hot or cold.")

#Exercise

name = input("Your name : ")
name_len = len(name)

if name_len < 3:
    print("Name must be atleast 3 characters")
elif name_len > 50:
    print("Name can be of maximum 50 characters")
else:
    print("Name looks good")