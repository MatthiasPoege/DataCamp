# Tip calculator

# Ask the user for the price
price = eval(input("Enter the price without tip: "))

# Ask for how much tip you want to give
tip_percent = eval(input("Enter the tip in Percent: "))

# calculate the tip and total bill
tip = price * tip_percent/100
final_price = price + tip

# print results
print("With a tip of ", tip_percent, "% you pay an additional ", tip, ".", sep="")
print("In total you have to pay ", final_price, ".", sep="")
