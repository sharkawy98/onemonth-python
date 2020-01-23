#######
# Write a script that takes a dollar amount and recommends a tip (15%, 18%, and 20%).
#######

#take user input
amount = input("Enter dollars amount: ")

#filter input from dollar sign and cast to float
amount = float(amount.replace("$", ""))

#print out the formatted tip amounts
print("These are different tip amounts for your entered dollars")
print(f"15% tip : {amount*0.15:.2f}")
print(f"18% tip : {amount*0.18:.2f}")
print(f"20% tip : {amount*0.2:.2f}")