#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: June 2021
# This program uses a function by reference

import string


def rounding_number(number):
    # Changes rounding by reference

    # Process and output
    number[0] = number[0] * (10 ** number[1]) + 0.5
    number[0] = int(number[0])
    number[0] = number[0] * (10 ** (-1 * number[1]))

    return 0


def main():
    # This function calls format_address

    number_var = []
    # Input
    print("Welcome!")
    number_input = input("Enter a number to round: ")
    decimal_input = input("Enter how many decimal places to round to: ")

    # Process and output
    try:
        number_float = float(number_input)
        decimals_integer = int(decimal_input)
        if decimals_integer >= 0:
            number_var.append(number_float)
            number_var.append(decimals_integer)

            # Call round_number
            rounding_number(number_var)
            print("The rounded number is {}".format(number_var[0]))
        else:
            print("Invalid.")
    except Exception:
        print("Invalid.")
    finally:
        print("\nThanks for participating!")


if __name__ == "__main__":
    main()
