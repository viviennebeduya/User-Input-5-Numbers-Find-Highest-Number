#set program's function to identify which is the highest number among the user's 5 inputs
def find_highest_number (number_one,number_two,number_three,number_four,number_five):
    #identify which number is the highest 
    #    if number 1 is greater than number 2, set number 1 as the highest number
    if number_one > number_two:
        highest_number = number_one
    #    else, set number 2 as the highest number
    else:
        highest_number = number_two
    #compare the remaining numbers to the current highest number
    #    if number 3 is greater than the highest number, set number 3 as the highest number
    #        else, the previous highest number remains 
    if number_three > highest_number:
        highest_number = number_three
    #    if number 4 is greater than the highest number, set number 4 as the highest number
    #        else, the previous highest number remains
    if number_four > highest_number:
        highest_number = number_four
    #    if number 5 is greater than the highest number, set number 5 as the highest number
    #        else, the previous highest number remains
    if number_five > highest_number:
        highest_number = number_five
    # return the highest number from the function
    return highest_number
#initialize user's input from number 1 to number 5
number_one = int(input("Input first number: "))
number_two = int(input("Input second number: "))
number_three = int(input("Input third number: "))
number_four = int(input("Input fourth number: "))
number_five = int(input("Input last number: "))
#print the function result
result = find_highest_number (number_one,number_two,number_three,number_four,number_five)
print (f"The highest number is {result}.")