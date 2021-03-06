# Prompt the user to enter a description for a product.
product = input("Please enter the description: ")

# Prompt the user to enter the quantity being purchased.
# Store the value as an integer. 
quantity = int(input(f"How many {product}'s would you like to order? "))

# Prompt the user to enter the regular price of the product. This value must be stored as a float.
regularAmount= float(input("What is the regular price? "))

# All of the products over $19.99 are 15% OFF
# All of the products over $39.99 are 25% OFF
print("Your Receipt")
print("----------------")
if regularAmount <= 19.99:
    newAmount = regularAmount 
    print(f"{quantity} {product}'s @ {newAmount:.2f} each")
elif regularAmount > 19.99 and regularAmount <= 39.99 :
    fifteen= regularAmount * .15
    newAmount = regularAmount - fifteen
    print(f"{quantity} {product}'s @ {newAmount:.2f} each")
elif regularAmount > 39.99 :
    twentyFive = regularAmount * .25 
    newAmount = regularAmount - twentyFive
    print(f"{quantity} {product}'s @ ${newAmount:.2f} each")
else: 
    print("Sorry there was an error on our end please try again!")
    
# Calculate the sales tax on the total purchase.  
# Assume a state sales tax rate of 6.5%.  
salesTax = (newAmount * quantity) * .065
print(f"Sales Tax : ${salesTax:.2f}")

# The rate should be calculated on the total price of the products after discount savings.
# Store this value as float in a variable.
totalWithDiscount = (newAmount* quantity) + salesTax
totalWithDiscount = float(totalWithDiscount)

# Display the total amount due from the customer.
print(f"Total amount due : ${totalWithDiscount:,.2f}")

# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.

#   *****thank you for your help here! my code turned read when i tried it and i thought it was wrong :)*****

# Display the total amount saved.
ogPrice = regularAmount * quantity
noDiscount = regularAmount == newAmount
youSaved = ogPrice - (quantity * newAmount)
if noDiscount :
    print("Thank you for shopping with us!")
else :
    print(f"You saved ${youSaved:,.2f} today!")


