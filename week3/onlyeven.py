# Create a file called "onlyeven.py"
# Prompt the user to enter a positive number
# Verify that the input is an integer and it is positive. Research the isDigit() method of the string 
# object. If it is not valid, prompt the user to re-enter until they enter a valid number.
# Create a function that displays only even numbers between and including 0 up to and including
#  (if valid) the number provided by the user.

# pos_num =input("Please enter a postive number: ")

# x = pos_num.isdigit() 
# while True:
#     pos_num = input("Invalid input. Please enter a postive number: ")
#     break
# while True:
#     pos_num = int(pos_num)
#     break


while True:
    try:
        pos_num =int(input("Please enter a postive number: "))
        if pos_num % 2 == 0:
            break 
    except:
        print("Invalid input. Please enter a postive number")

print("--------")

for current_num in range(pos_num+1,):
    if current_num % 2 == 0:
        print(current_num)

