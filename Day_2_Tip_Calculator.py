# If the bill was $150.00, split between 5 people, with 12% tip
# Each person should pay (150.00 / 5) * 1.12
# Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_perc   = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
party_size = int(input("How many people to plit the bill? "))

# total_bill_float = float(total_bill)
# tip_perc_int     = int(tip_perc)
# party_size_int   = int(party_size)

split_amount = total_bill * (tip_perc / 100.0 + 1.0) / party_size
split_amount_round = round(split_amount,2)

print(f"Each person should pay: ${split_amount_round}")


