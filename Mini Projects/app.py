#1.Enter the weight either in Kgs or in pounds it will return the converted value

# weight = int(input("Weight : "))
# unit = input("(L) for lbs and (K) for kgs : ")

# if unit.upper() == "L":
#     weight = weight/2.20462
#     print(f"Weight : {weight} kgs")
# elif unit.upper() == "K":
#     weight = weight*2.20462
#     print(f"Weight : {weight} lbs")

#2. Car game 
command =""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if  command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to end the game
            """)
    elif command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:  
            started = False  
            print("Car stopped...")
    elif command == "quit":
        print("Thanks for playing")
        break
    else:
        print("Invalid command")


 