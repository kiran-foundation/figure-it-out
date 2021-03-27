from fio.figure_it_out import *
from PIL import Image

import math


def main():
    input_val = take_input()
    convert_val = convert_str_float(input_val[0], input_val[1], input_val[2], input_val[3])
    final_val = find_body_type(convert_val[0], convert_val[1], convert_val[2], convert_val[3])

    if type(final_val) == tuple:
        print(f"Your body type is :{final_val[0]}")
        print(f"Description: {final_val[2]}")
        print(f"Click this link for more info: {final_val[3]}")
        img = Image.open(final_val[1])  # image
        img.show()
    else:
        print(final_val)

    str_repeat = repeat()
    if str_repeat == 'Y' or str_repeat == 'y':
        main()
    else:
        exit()


# validate() function validates the input
def take_input():
    # Input Bust Size, input_val[0]

    bust_val = input("Enter Bust Size: ")

    # Validating bust size

    while bust_val == '' or bust_val.isspace() or float(bust_val) <= 9 or float(bust_val) >= 100:
        bust_val = input(
            "Bust size is invalid! Enter numeric value in inch and Please enter your value in range of (9 - 99 )")

    # Input Waist Size #
    waist_val = input("Enter Waist Size: ")

    # Validating waist size
    while waist_val == '' or waist_val.isspace() or float(waist_val) <= 9 or float(waist_val) >= 100:
        bust_val = input(
            "Bust size is invalid! Enter numeric value in inch and Please enter your value in range of (9 - 99 )")

    # Input Hip Size #
    hip_val = input("Enter hip Size: ")

    # Validating hip size
    while hip_val == '' or hip_val.isspace() or float(hip_val) <= 9 or float(hip_val) >= 100:
        bust_val = input(
            "Bust size is invalid! Enter numeric value in inch and Please enter your value in range of (9 - 99 )")

    # Input High Hip Size

    highhip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while highhip_val == '' or highhip_val.isspace() or float(highhip_val) <= 9 or float(highhip_val) >= 100:
        bust_val = input(
            "Bust size is invalid! Enter numeric value in inch and Please enter your value in range of (9 - 99 )")

    return bust_val, waist_val, hip_val, highhip_val


# convert_str_float() converts string into float
def convert_str_float(str1, str2, str3, str4):
    bust_floatval = float(str1)
    waist_floatval = float(str2)
    hip_floatval = float(str3)
    highhip_floatval = float(str4)

    return bust_floatval, waist_floatval, hip_floatval, highhip_floatval


# repeat() asks user whether to continue or not
def repeat():
    val = input("Do you want to continue: Type Y or N: ")
    return val


main()
