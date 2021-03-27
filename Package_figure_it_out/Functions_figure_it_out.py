from Package_figure_it_out.Dictionary_figure_it_out import *

# figure_it_out() returns dictionary


def find_body_type(bust, waist, hip, high_hip):
    if bust - hip <= 2 and bust - hip > 0 and bust - waist >= 8  or  hip-bust  <= 2 and hip-bust > 0 and hip - waist >= 8:
        return body_type_dict['hourglasse'],body_type_image_dict['hourglasse'],body_type_desc_dict['hourglasse'],body_type_URL_dict['hourglasse']
    if hip - bust >= 6 and hip - waist >= 8 and bust - waist > 0 and hip-high_hip <= 5:
        return body_type_dict['spoon'],body_type_image_dict['spoon'],body_type_desc_dict['spoon'],body_type_URL_dict['spoon']
    if hip - bust >= 6 and hip - waist >= 8 and bust - waist > 0 and hip-high_hip > 5:
        return body_type_dict['triangle'], body_type_image_dict['triangle'], body_type_desc_dict['triangle'], body_type_URL_dict['triangle']
    if bust - hip > 1 and hip - bust < 0  and bust - waist >= 5:
        return body_type_dict['inverted triangle'],body_type_image_dict['inverted triangle'],body_type_desc_dict['inverted triangle'],body_type_URL_dict['inverted triangle']
    if hip - bust <= 3 and bust-hip < 2  and bust - waist < 3 and bust - waist >= 0 and hip - waist < 3 and hip-waist >0:
        return body_type_dict['rectangle'],body_type_image_dict['rectangle'],body_type_desc_dict['rectangle'],body_type_URL_dict['rectangle']
    if bust-waist < 0  and hip-waist < 0 and hip- bust <= 3 and hip- bust >0 or bust-waist < 0  and hip-waist < 0 and bust-hip <= 3 and bust-hip >0:
        return body_type_dict['diamond'],body_type_image_dict['diamond'],body_type_desc_dict['diamond'],body_type_URL_dict['diamond']
    if bust-waist < 0  and hip-waist < 0 and hip- bust > 3 or bust-waist < 0  and hip-waist < 0 and bust - hip > 3:
        return body_type_dict['oval'],body_type_image_dict['oval'],body_type_desc_dict['oval'],body_type_URL_dict['oval']
    else:
        return "Invalid Measurements"

# validate() function validates the input
def validate():
    # Input Bust Size
    global bust_val
    bust_val = input("Enter Bust Size: ")

    # Validating bust size
    while bust_val == '' or bust_val.isspace():
        bust_val = input("Bust size is invalid! Enter numeric value in inch: ")

    # Input Waist Size
    global waist_val
    waist_val = input("Enter Waist Size: ")

    # Validating waist size
    while waist_val == '' or waist_val.isspace():
        waist_val = input("Waist size is invalid! Enter numeric value in inch: ")

    # Input Hip Size
    global hip_val
    hip_val = input("Enter hip Size: ")

    # Validating hip size
    while hip_val == '' or hip_val.isspace():
        hip_val = input("Hip size is invalid! Enter numeric value in inch: ")

    # Input High Hip Size
    global highhip_val
    highhip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while highhip_val == '' or highhip_val.isspace():
        highhip_val = input("High Hip size is invalid! Enter numeric value in inch: ")

    return bust_val, waist_val, hip_val, highhip_val

# convert_str_float() converts string into float


def convert_str_float(str1, str2, str3, str4):
    global bust_floatval, waist_floatval, hip_floatval, highhip_floatval
    bust_floatval = float(str1)
    waist_floatval = float(str2)
    hip_floatval = float(str3)
    highhip_floatval = float(str4)
    return bust_floatval, waist_floatval, hip_floatval, highhip_floatval

# repeat() asks user whether to continue or not
def repeat():

    val = input("Do you want to continue: Type Y or N: ")
    return val
