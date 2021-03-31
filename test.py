# validate function validates input for empty value and string value
def validate():
    # Input Bust Size
    global bust_val
    bust_val = input("Enter Bust Size: ")

    # Validating bust size
    while bust_val == '' or bust_val.isspace():
        bust_val = input("Bust size is invalid.html! Enter numeric value in inch: ")

    # Input Waist Size
    global waist_val
    waist_val = input("Enter Waist Size: ")

    # Validating waist size
    while waist_val == '' or waist_val.isspace():
        waist_val = input("Waist size is invalid.html! Enter numeric value in inch: ")

    # Input Hip Size
    global hip_val
    hip_val = input("Enter hip Size: ")

    # Validating hip size
    while hip_val == '' or hip_val.isspace():
        hip_val = input("Hip size is invalid.html! Enter numeric value in inch: ")

    # Input High Hip Size
    global high_hip_val
    high_hip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while high_hip_val == '' or high_hip_val.isspace():
        high_hip_val = input("High Hip size is invalid.html! Enter numeric value in inch: ")


# function to define the body type based on conditions


def figure_it_out():
    validate()
    bust_intval = int(bust_val)
    hip_intval = int(hip_val)
    waist_intval = int(waist_val)
    high_hip_intval = int(high_hip_val)
    print(type(bust_intval))
    # Printing entered values
    print("\nMeasurements are:\n")
    print(f"Bust Size is: {bust_intval}")
    print(f"Waist Size is: {waist_intval}")
    print(f"Hip Size is: {hip_intval}")
    print(f"High Hip Size is: {high_hip_intval}")


    if (bust_intval - hip_intval) <= 1 and (hip_intval - bust_intval) <= 3.6 and (bust_intval - waist_intval) >= 9 or (
            hip_intval - waist_intval) >= 10:
        print("your body size match to Hourglass categary,"
              "suitable style:  Narrow v nack, Dark top, Jackets, Tailor shirts")

        # For Bottom hourglass

    if (hip_intval - bust_intval) >= 3.6 and (hip_intval - bust_intval) < 10 and (hip_intval - waist_intval) >= 9 and (
            high_hip_intval - waist_intval) < 1.193:
        print("Your body size match to Bottom hourglass categary,"
              "suitable style: ")
        # To do dress style

        # For Top hourglass

    if (bust_intval - hip_intval) > 2 and (hip_intval - waist_intval) >= 7 and (bust_intval - waist_intval) >= 1.2:
        print("Your body size match to Top Hourglss categary,"
              "suitable syle : narrow V-necks. You should also try wearing dark tops."
              " A couple of jackets and well-tailored shirts")

        # For Spoon

    if (hip_intval - bust_intval) > 4 and (hip_intval - waist_intval) >= 9:
        print("Your body size match to spoon categary,"
              "suitable style :A-line skirts, boot cut jeans or trousers, mid-rise jeans, padded bras, "
              "chunky earrings and necklaces, well-defined shouldered jackets,")

        # For Triangle
    if (hip_intval - bust_intval) >= 3 and (hip_intval - waist_intval) < 6:
        print("Your body size match to Tringle categary,"
              "suitable style : Wear bright scoop-neck and boat-neck tops. This will make your shoulders look wider")

        # For Inverted triangle
    if (bust_intval - hip_intval) >= 4 and (bust_intval - waist_intval) < 5:
        print("Your body size match to Inverted triangle body shape, These "
              "suitable style :Wear soft-textured fabrics, A-line dresses, "
              "shirts with a tie below the bust line, tops that fall lower than the hip bone,"
              " tops with cuff sleeves, well-fitting clothes, V-necks, scoop tops, ruched t-shirts")

        # For Rectangle
    if (hip_intval - bust_intval) < 3 and (bust_intval - hip_intval) < 3 and (bust_intval - waist_intval) < 3 and (
            hip_intval - waist_intval) < 3:
        print("Your body size match to Rectangle body shape,"
              "suitalbe style : Tube tops and Polka dress")


figure_it_out()
