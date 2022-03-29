# Prompt the user to enter a description for a product.
product = input("Please enter the description: ")

# Prompt the user to enter the quantity being purchased. 
amount = input(f"How many {product}'s would you like to order? ")

# Store the value as an integer.
amount = int(amount)

# Prompt the user to enter the regular price of the product. This value must be stored as a float.
regularAmount= input("What is the regular price? ")
regularAmount = float(regularAmount)

# All of the products over $19.99 are 15% OFF
# All of the products over $39.99 are 25% OFF
print("Your Receipt")
print("----------------")
if regularAmount <= 19.99:
    newAmount = regularAmount 
    print(f"{amount} {product}'s @ {newAmount:.2f} each ")
elif regularAmount > 19.99 and regularAmount <= 39.99 :
    fifteen= regularAmount * .15
    newAmount = regularAmount - fifteen
    print(f"{amount} {product}'s @ {newAmount:.2f} each")
elif regularAmount > 39.99 :
    twentyFive = regularAmount * .25 
    newAmount = regularAmount - twentyFive
    print(f"{amount} {product}'s @ ${newAmount:.2f} each")
else: 
    print("Sorry there was an error on our end please try again!")
    
# Calculate the sales tax on the total purchase.  
# Assume a state sales tax rate of 6.5%.  
salesTax = (newAmount * amount) * .065

print(f"Sales Tax : ${salesTax:.2f}")

# The rate should be calculated on the total price of the products after discount savings.
# Store this value as float in a variable.
totalWithDiscount = (newAmount* amount) + salesTax
totalWithDiscount = float(totalWithDiscount)

# Display the total amount due from the customer.
print(f"Total amount due : ${totalWithDiscount:,.2f}")

# Format the output as a fixed point number with two-decimal places, a comma as a thousand separator and the dollar sign.

#   *****IM A BIT LOST ON THIS PART!*****

# Display the total amount saved.
ogPrice = regularAmount * amount
noDiscount = regularAmount == newAmount
youSaved = ogPrice - (amount * newAmount)
if noDiscount :
    print("Thank you for shopping with us!")
else :
    print(f"You saved ${youSaved:.2f} today!")


