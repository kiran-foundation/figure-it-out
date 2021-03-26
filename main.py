from fio.figure_it_out import *
from PIL import Image


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
    # Input Bust Size
    global bust_val
    bust_val = 0
    bust_val = input("Enter Bust Size: ")

    # Validating bust size
    while bust_val == '' or bust_val.isspace():
        bust_val = input("Bust size is invalid! Enter numeric value in inch: ")

    while not float(bust_val) in range(9, 99):
        bust_val = input("Please enter your value in range of (9 - 99 )")

    # Input Waist Size
    global waist_val
    waist_val = 0
    waist_val = input("Enter Waist Size: ")


    # Validating waist size
    while waist_val == '' or waist_val.isspace():
        waist_val = input("Waist size is invalid! Enter numeric value in inch: ")

    while not float(waist_val) in range(9, 99):
        waist_val = input("Please enter your value in range of (9 - 99 )")


    # Input Hip Size
    global hip_val
    hip_val = 0
    hip_val = input("Enter hip Size: ")

    # Validating hip size
    while hip_val == '' or hip_val.isspace():
        hip_val = input("Hip size is invalid! Enter numeric value in inch: ")

    while not float(hip_val) in range(9, 99):
        hip_val = input("Please enter your value in range of (9 - 99 )")

    # Input High Hip Size
    global highhip_val
    hip_val = 0
    highhip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while highhip_val == '' or highhip_val.isspace():
        highhip_val = input("High Hip size is invalid! Enter numeric value in inch: ")
    while not float(highhip_val) in range(9, 99):
        highhip_val = input("Please enter your value in range of (9 - 99 )")

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


