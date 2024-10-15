#set program's function to identify which is the highest number among the user's 5 inputs
def find_highest_number (number1,number2,number3,number4,number5):
    #identify which number is the highest 
    #    if number 1 is greater than number 2, set number 1 as the highest number
    if number1 > number2:
        highest_number = number1
    #    else, set number 2 as the highest number
    else:
        highest_number = number2
    #compare the remaining numbers to the current highest number
    #    if number 3 is greater than the highest number, set number 3 as the highest number
    #        else, the previous highest number remains
    if number3 > highest_number:
        highest_number = number3
    #    if number 4 is greater than the highest number, set number 4 as the highest number
    #        else, the previous highest number remains
    if number4 > highest_number:
        highest_number = number4
    #    if number 5 is greater than the highest number, set number 5 as the highest number
    #        else, the previous highest number remains
    if number5 > highest_number:
        highest_number = number5
    # return the highest number from the function
    return highest_number
#initialize user's input from number 1 to number 5
number1 = int(input("Input first number: "))
number2 = int(input("Input second number: "))
number3 = int(input("Input third number: "))
number4 = int(input("Input fourth number: "))
number5 = int(input("Input last number: "))
#print the function result
result = find_highest_number (number1,number2,number3,number4,number5)
print (f"The highest number is {result}.")