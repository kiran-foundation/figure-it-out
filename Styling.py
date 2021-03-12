# validate function validates input for empty value and string value
def validate():
    # Input Bust Size
    global bust_val
    bust_val = input("Enter Bust Size: ")

    # Validating bust size
    while bust_val == '' or bust_val.isspace():
        bust_val = input("Bust size is invalid! Enter numeric value: ")

    # Input Waist Size
    global waist_val
    waist_val = input("Enter Waist Size: ")

    # Validating waist size
    while waist_val == '' or waist_val.isspace():
        waist_val = input("Waist size is invalid! Enter numeric value: ")

    # Input Hip Size
    global hip_val
    hip_val = input("Enter hip Size: ")

    # Validating hip size
    while hip_val == '' or hip_val.isspace():
        hip_val = input("Hip size is invalid! Enter numeric value: ")

    # Input High Hip Size
    global high_hip_val
    high_hip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while high_hip_val == '' or high_hip_val.isspace():
        high_hip_val = input("High Hip size is invalid! Enter numeric value: ")

# function to define the body type based on conditions


class Hourglass(object):
    pass


def figure_it_out():
    validate()

    # Printing entered values
    print("\nMeasurements are:\n")
    print(f"Bust Size is: {bust_val}")
    print(f"Waist Size is: {waist_val}")
    print(f"Hip Size is: {hip_val}")
    print(f"High Hip Size is: {high_hip_val}")

    # TODO print body type based on measurements

    # For Hourglass

    if int(bust_val) - int(hip_val) <= 1 and int(hip_val) - int(bust_val)<= 3.5 and int(bust_val) - int(waist_val) >= 9 or int(hip_val) - int(waist_val) >= 10:
        print("your body size match to Hourglass categary,These tipes are pattern suit on you:")
           # Narrow v nack, Dark top, Jackets, Tailor shirts,

    # For Bottom hourglass
    if int(hip_val) - int(bust_val) >= 3.6 and int(hip_val) - int(bust_val) < 10 and int(hip_val) - int(waist_val) >= 9 and int(high_hip_val) / int(waist_val) < 1.193:
       print("Your body size match to Bottom hourglass categary, These tipes are pattern suit on you:")
            # To do dress style

    # For Top hourglass
    if int(bust_val) - int(hip_val) > 1 and int(bust_val) - int(hip_val) < 10 and int(bust_val) - int(waist_val) >= 9:
        print("Your body size match to Top Hourglss categary, These tipes are pattern suit on you:")
        # narrow V-necks. You should also try wearing dark tops. A couple of jackets and well-tailored shirts

    # For Spoon
    if int(hip_val) - int(bust_val) > 2 and int(hip_val) - int(waist_val) >= 7 and int(high_hip_val)/int(waist_val) >= 1.193:
        print("Your body size match to spoon categary, These tipes are pattern suit on you:")
        # A-line skirts, boot cut jeans or trousers, mid-rise jeans, padded bras, chunky earrings and necklaces, well-defined shouldered jackets,

    # For Triangle
    if int(hip_val) - int(bust_val) >= 3.6 and int(hip_val) - int(waist_val) < 9:
        print("Your body size match to Tringle categary, These tipes are pattern suit on you:")
        # Wear bright scoop-neck and boat-neck tops. This will make your shoulders look wider

    # For Inverted triangle
    if int(bust_val) - int(hip_val) >= 3.6 and int(bust_val) - int(waist_val) < 9:
        print("Your body size match to Inverted triangle body shape, These tipes are pattern suit on you:")
        # Wear soft-textured fabrics, A-line dresses, shirts with a tie below the bust line, tops that fall lower than the hip bone, tops with cuff sleeves, well-fitting clothes, V-necks, scoop tops, ruched t-shirts

    # For Rectangle
    if int(hip_val) - int(bust_val) < 3.6 and int(bust_val) - int(hip_val) < 3.6 and int(bust_val) - int(waist_val) < 9 and int(hip_val) - int(waist_val) < 10:
        print("Your body size match to Rectangle body shape,These tipes are pattern suit on you:")
        #Tube tops and Polka dress

figure_it_out()

