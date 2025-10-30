#!/usr/bin/env python3
# Created By: Abdul
# Date: 10/27/2025
# Program to ask the user for an integer


def main():
    # get user input and handle exceptions
    try:
        age = input("Please enter your age: ")
        age = int(age)
        # check if the age is within the allowed range
        if age > 25 and age < 40:
            print("You can date my grandchild.")
        else:
            print("Sorry, you are not eligible to date my grandchild.")

    # if user input is not an integer, catch the exception
    except ValueError:
        print(age, "is not an integer.")
    # display ending message to user no matter the outcome
    finally:
        print("Thanks for trying!")


if __name__ == "__main__":
    main()
