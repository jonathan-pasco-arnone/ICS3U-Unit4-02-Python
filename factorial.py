#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program determines the factorial of a positive integer


def main():
    # This function determines the factorial of a positive integer

    print("")
    print("This program calculates the factorial of a positive integer")
    print("")
    number_str = input("Please enter a positive integer: ")
    answer = 1
    print("")

    try:
        number = int(number_str)
    except Exception:
        print("Invalid Input")
    else:
        if number > 0:
            answer = answer * number
            number = number - 1
            while (number > 0):
                answer = answer * number
                number = number - 1
            answer_str = str(answer)
            print("The factorial of " + number_str + " is " + answer_str)
        elif number == 0:
            print("The factorial of 0 is 1")
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
