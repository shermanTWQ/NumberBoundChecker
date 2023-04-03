import random
import math

#Number Bound Check
#Provided for non-commercial use. Please refer to Github Repo for more information.
#Contact: Sherman_tan@outlook.com
#(C) Tan Wei Qiang Sherman.

lower = int(input("Enter Lower bound number: "))

upper = int(input("Enter Upper number:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the hidden integer!\n")

count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations you did it in ", count, " tries.")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("Number is too small!")
    elif x < guess:
        print("Number is  too high!")

if count >= math.log(upper - lower + 1, 2):
    print("\nSorry, the hidden number is %d." % x)


