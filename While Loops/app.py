# i = 1

# while i<=5:
#     print('*'*i)
#     i += 1

# print("done")

#Exercise :  a guessing game

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    user_guess = int(input("Guess : "))
    guess_count += 1
    if(user_guess == secret_number):
        print("You won!")
        break
else:
    print("You Failed!")        
