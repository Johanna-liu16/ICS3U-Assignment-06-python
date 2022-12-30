#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program calculates the area of a trapezoid

import math  # for rounding


def calculate_area(base_one: float, height: float, base_two: float) -> float:
    # calculate area

    area = (base_one + base_two) / 2 * height
    return area


def main():
    # input
    print("This program calculates the area of a trapezoid.")
    str_base_one = input("Enter length of the first base (cm): ")
    str_base_two = input("Enter length of the second base (cm): ")
    str_height = input("Enter length of height (cm): ")

    try:
        base_one = float(str_base_one)
        base_two = float(str_base_two)
        height = int(str_height)
        if base_one < 0 or base_two < 0 or height < 0:
            print("Invalid Input")
        # call functions
        total_area = calculate_area(base_one, height, base_two)
        print("The area of a trapezoid is {0} cm²".format(round(total_area, 2)))
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
