
# validate function validates input for empty value and string value
def validate():
    # Input Bust Size
    global int_bust
    int_bust = input("Enter Bust Size: ")

    # Validating bust size
    while int_bust == '':
        int_bust = input("Bust size can not be empty! Enter Bust Size: ")

    while not int_bust.isdigit():
        int_bust = input("Bust size can not be string! Enter numeric value: ")

    # Input Waist Size
    global int_waist
    int_waist = input("Enter Waist Size: ")

    # Validating waist size
    while int_waist == '':
        int_waist = input("Waist size can not be empty! Enter waist Size: ")

    while not int_waist.isdigit():
        int_waist = input("Waist size can not be string! Enter numeric value: ")

    # Input Hip Size
    global int_hip
    int_hip = input("Enter hip Size: ")

    # Validating hip size
    while int_hip == '':
        int_hip = input("Hip size can not be empty! Enter hip Size: ")

    while not int_hip.isdigit():
        int_hip = input("Hip size can not be string! Enter numeric value: ")

    # Input High Hip Size
    global int_highhip
    int_highhip = input("Enter High hip Size: ")

    # Validating high hip size
    while int_highhip == '':
        int_highhip = input("High hip size can not be empty! Enter High hip Size: ")

    while not int_highhip.isdigit():
        int_highhip = input("High Hip size can not be string! Enter numeric value: ")

# function to define the body type based on conditions
def figure_it_out():
    validate()

    # Printing entered values
    print("\nMeasurements are:\n")
    print(f"Bust Size is: {int_bust}")
    print(f"Waist Size is: {int_waist}")
    print(f"Hip Size is: {int_hip}")
    print(f"High Hip Size is: {int_highhip}")

    #TODO print body type based on measurements

figure_it_out()