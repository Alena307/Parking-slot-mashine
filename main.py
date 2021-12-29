# Write your code below this line 
bill = input("What are your parking costs?")
bill1 = float(bill)
people = input("How many people pay the bill?")
people1 = int(people)
#print(people)
result = round(bill1 / people1,2)
#print(result)
print(f"Everyone should pay {result} Euros.\nLet's go to the parking slot mashine.")
