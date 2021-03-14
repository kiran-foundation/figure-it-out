# validate function validates input for empty value and string value
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
    global high_hip_val
    high_hip_val = input("Enter High hip Size: ")

    # Validating high hip size
    while high_hip_val == '' or high_hip_val.isspace():
        high_hip_val = input("High Hip size is invalid! Enter numeric value in inch: ")

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

    if int(bust_val) - int(hip_val) <= 1 and int(hip_val) - int(bust_val)<= 3.6 and int(bust_val) - int(waist_val) >= 9 or int(hip_val) - int(waist_val) >= 10:
        print("your body size match to Hourglass categary,"
              "suitable style: Narrow v nack, Dark top, Jackets, Tailor shirts,")


    # For Bottom hourglass
    if int(hip_val) - int(bust_val) >= 3.6 and int(hip_val) - int(bust_val) < 10 and int(hip_val) - int(waist_val) >= 9 and int(high_hip_val) / int(waist_val) < 1.193:
       print("Your body size match to Bottom hourglass categary, These tipes are pattern suit on you:")
            # To do dress style

    # For Top hourglass
    if int(bust_val) - int(hip_val) > 2 and int(bust_val) - int(hip_val) >= 7 and int(bust_val) - int(waist_val) >= 1.2:
        print("Your body size match to Top Hourglss categary,"
              "# narrow V-necks. You should also try wearing dark tops. A couple of jackets and well-tailored shirts:")


    # For Spoon
    if int(hip_val) - int(bust_val) > 4 and int(hip_val) - int(waist_val) <= 9 :
        print("Your body size match to spoon categary, "
              "suitable style : A-line skirts, boot cut jeans or trousers, mid-rise jeans, padded bras,"
              " chunky earrings and necklaces, well-defined shouldered jackets,:")


    # For Triangle
    if int(hip_val) - int(bust_val) >= 3 and int(hip_val) - int(waist_val) < 6:
        print("Your body size match to Tringle categary,"
              "SUITABLE STYLE : Wear bright scoop-neck and boat-neck tops. This will make your shoulders look wider"
              'Emphasise your shoulders and bust to balance your silhouette.'
               'Accentuate your top half – wear bright colours and accessories, prints and mix your textures and volumes.'
               'Tone down your lower half – keep things discrete with dark colours and neutrals.'
               'Choose wide-legged, straight-cut and flared trousers and jeans.'
               'Go for plunging necklines.'
              ' Embrace A-line and princess cuts for skirts and dresses')


    # For Inverted triangle
    if int(bust_val) - int(hip_val) >= 4 and int(bust_val) - int(waist_val) >5  :
        print("Your body size match to Inverted triangle body shape, "
              "suitable style:# Wear soft-textured fabrics, A-line dresses, shirts with a tie below the bust line, "
              "tops that fall lower than the hip bone, tops with cuff sleeves, well-fitting clothes, V-necks, scoop tops, ruched t-shirts")


    # For Rectangle
    if int(hip_val) - int(bust_val) < 3 and int(bust_val) - int(hip_val) < 3 and int(bust_val) - int(waist_val) < 3 and int(hip_val) - int(waist_val) < 4:
        print("Your body size match to Rectangle body shape,"
              'SUITABLE STYLE :Choose asymmetrical cuts to create curves.'
              'Pick skirts and dresses that are cinched at the waist.'
              'Opt for fitted, structured blazers and jackets.'
              'Look for straight, wide-legged and flared trousers and jeans (go high-waisted if you want a slim fit')

    # For Diamond
    if int(waist_val)- int(bust_val) >= 1 and int(hip_val)-int(bust_val)< 2:
        print('This body shape has a thicker waist circumference than the bust round or hip round.The stomach area may appear protruding.'
              ' Some may call it an Apple when the upper body is slightly bigger than the hip.'
              'SUITABLE STYLE : you should dress in such a way to hide your tummy by jackets, duppattas or dreping style dress'
              )

    #  FOR oval
    if int(bust_val)-int(waist_val) <= 0 and int(bust_val)-int(hip_val)> 1:
        print('Your waist is broader than your shoulders or hips.'
               'You’re generally well-proportioned.'
               'You have a fuller bust/upper body.'
               'Your waist is undefined.'
              'SUITABLE STYLE : Opt for silhouettes without structured waistlines to take focus away from the mid-section.'
               'Choose bust-defining tops in dark colours and diagonal/vertical stripes.'
               'Your Power Pieces:'
               'Go for a V-neck or a round neck and peplum tops.'
               'Pick high-waisted, slim fit and straight-leg trousers and jeans.'
               'Opt for high-waisted, pencil and A-line skirts.'
               'Choose imperial cut and strapless dresses.'
               'Bring in under-bust belts.')


figure_it_out()

