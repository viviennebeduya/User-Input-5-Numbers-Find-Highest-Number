#set program's function to identify which is the highest number among the user's 5 inputs
    #identify which number is the highest 
    #    if number 1 is greater than number 2, set number 1 as the highest number
    #    else, set number 2 as the highest number
    #compare the remaining numbers to the current highest number
    #    if number 3 is greater than the highest number, set number 3 as the highest number
    #        else, the previous highest number remains
    #    if number 4 is greater than the highest number, set number 4 as the highest number
    #        else, the previous highest number remains
    #    if number 5 is greater than the highest number, set number 5 as the highest number
    #        else, the previous highest number remains
    # return the highest number from the function
#initialize user's input from number 1 to number 5
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))
num3 = int(input("Input third number: "))
num4 = int(input("Input fourth number: "))
num5 = int(input("Input last number: "))
#print the function result