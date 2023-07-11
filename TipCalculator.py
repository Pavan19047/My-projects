print("Welcome to the tip Calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percent of tip you would like to give? 10,12 or 15? "))
split = int(input("How many people to split the bill? "))
tip_perc = tip / 100
tip_amt = tip_perc * bill
total_bill = bill + tip_amt
bill_per_person = total_bill / split
final_amt = round(bill_per_person,2)
final_amt = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_amt}")