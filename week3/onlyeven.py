
# Create a file called "onlyeven.py"
# Prompt the user to enter a positive number
# Verify that the input is an integer and it is positive. Research the isDigit() method of the string 
# object. If it is not valid, prompt the user to re-enter until they enter a valid number.
# Create a function that displays only even numbers between and including 0 up to and including
#  (if valid) the number provided by the user.


# while True:
#     try:
#         pos_num =int(input("Please enter a positive number: "))
#         if pos_num % 2 == 0:
#             break 
#     except:
#         print("Invalid input. Please enter a positive number")

# print("--------")

# for current_num in range(pos_num+1):
#     if current_num % 2 == 0:
#         print(current_num)


# ********* Sorry I was making this really complicated. I thought I could only accept an even number as the input! ***********
# thank you for clearing that up!! 


while True:
    user_number = input("Please enter a postive number: ")
    if(user_number.isdigit() and (int(user_number)> 0)):
        break 
    print("Invalid input.", end=" ")



print("--------")

for current_num in range(int(user_number)+1):
    if current_num % 2 == 0:
        print(current_num)