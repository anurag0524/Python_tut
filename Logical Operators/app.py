hasHighIncome = True
hasGoodCredit = True
hasCriminalRecord = False

#Logical and
# if hasHighIncome and hasGoodCredit:
#     print("Eligible for loan")
# else: 
#     print("Not eligible for loan")

#Logical or
# if hasHighIncome or hasGoodCredit:
#     print("Eligible for loan")
# else: 
#     print("Not eligible for loan")  
    
#Not Operator(reverses a boolean value)
if hasGoodCredit and not hasCriminalRecord:
    print("Eligible for loan")
else:
    print("Not eligible for loan")