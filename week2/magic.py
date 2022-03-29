# Prompt the user to input a number.
FirstNumber = int(input("Please enter a number: "))
# Multiple this number by 3.
multiNumber = (FirstNumber * 3)
# Add 6 to the number
thenAdd = (multiNumber + 6)
# Divide the new number by 3.
thenDivide= (thenAdd // 3)
# Subtract the number from step 1 from the answer in step 4.
thenSubtract = (thenDivide - FirstNumber)
# Display the results as an integer.  The results should always be 2. 
print(thenSubtract)