print("Welcome to the tip calculator.")
bill = float(input("How much is the Bill? $"))
tip = int(input("How much tip would you like to give? 10,12 or 15?"))
people = int(input("To how many people is the bill being split?"))

tip_percent = tip/100
tip_amount = tip_percent * bill
total_bill = bill + tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}")
