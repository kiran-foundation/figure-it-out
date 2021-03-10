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
    global highhip_val
    highhip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while highhip_val == '' or highhip_val.isspace():
        highhip_val = input("High Hip size is invalid! Enter numeric value: ")

# function to define the body type based on conditions


def figure_it_out():
    validate()

    # Printing entered values
    print("\nMeasurements are:\n")
    print(f"Bust Size is: {bust_val}")
    print(f"Waist Size is: {waist_val}")
    print(f"Hip Size is: {hip_val}")
    print(f"High Hip Size is: {highhip_val}")

    # TODO print body type based on measurements


figure_it_out()

