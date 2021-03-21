# Install PILLOW library to work with images
from PIL import Image


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


# convert_str_float() converts string into float
def convert_str_float():
    global bust_floatval, waist_floatval, hip_floatval, highhip_floatval
    bust_floatval = float(bust_val)
    waist_floatval = float(waist_val)
    hip_floatval = float(hip_val)
    highhip_floatval = float(highhip_val)


# figure_it_out() decides body type and dressing style
def figure_it_out():

    validate()
    convert_str_float()

    # Printing entered values
    print("\nMeasurements are:\n")
    print(f"Bust Size is: {bust_floatval}")
    print(f"Waist Size is: {waist_floatval}")
    print(f"Hip Size is: {hip_floatval}")
    print(f"High Hip Size is: {highhip_floatval}")

'''   # For Hourglass
    if bust_floatval - hip_floatval <= 1 and hip_floatval - bust_floatval <= 3.6 and bust_floatval - waist_floatval >= 9 or hip_floatval - waist_floatval >= 10:
        print("Hello dear your body type belongs  HOURGLASS category")
        print("SUITABLE STYLE YOU LOOK BEST IN ::  Narrow v neck, Dark top, Jackets, Tailor shirts. For more info, "
              "click below link: ")
        print("https://40plusstyle.com/how-to-dress-the-hourglass-shape/")
        print("img.png") # image
        repeat()

    # For Bottom hourglass
    if bust_floatval-hip_floatval> 1 and bust_floatval-hip_floatval<10 and bust_floatval-waist_floatval>=9:
        print(" Hello dear your body type belongs to BOTTOM HOURGLASS category")
        print("SUITABLE STYLES IN YOU LOOK BEST :: These types of pattern suit on you: <fill dressing types here>. For more info, "
              "click below link: ")
        print("https://www.savitude.com/bottom-hourglass")
        repeat()

    # For Top hourglass
    if hip_floatval-bust_floatval >2 and hip_floatval-waist_floatval >=7 and highhip_floatval-waist_floatval > 1.2:
        print("Hello dear your body type belongs to TOP HOURGLASS category")
        print("SUITABLE STYLE YOU LOOK BEST IN :: These types of pattern suit on you: Narrow V-necks. You should also try wearing dark tops. A couple of "
              "jackets and well-tailored shirts. For more info, click below link: ")
        print("https://www.savitude.com/top-hourglass")
        repeat()

    # For Spoon
    if hip_floatval - bust_floatval >= 4 and hip_floatval- waist_floatval < 9:
        print("Hello dear your body type belongs to SPOON category")
        print(" SUITABLE STYLE YOU LOOK BEST IN :: A-line skirts, boot cut jeans or trousers, mid-rise jeans, "
              "padded bras, chunky earrings and necklaces, well-defined shouldered jackets. For more info, "
              "click below link: ")
        print("https://shilpaahuja.com/dressing-tips-spoon-body-type/")
        repeat()

    # For Triangle
    if hip_floatval-bust_floatval >=3 and bust_floatval-waist_floatval <6:
        print("Hello dear your body type belongs to TRIANGLE category")
        print("SUITABLE STYLE YOU LOOK BEST IN :: Wear bright scoop-neck and boat-neck tops. This will make your shoulders look wider. "
              "Emphasise your shoulders and bust to balance your silhouette. Accentuate your top half – wear bright "
              "colours and accessories, prints and mix your textures and volumes. Tone down your lower half – keep "
              "things discrete with dark colours and neutrals. Choose wide-legged, straight-cut and flared trousers "
              "and jeans. Go for plunging necklines. Embrace A-line and princess cuts for skirts and dresses. For "
              "more info, click below link: ")
        print("https://lookiero.co.uk/blog/how-dress-triangle-body-shape/")
        repeat()

    # For Inverted triangle
    if bust_floatval - hip_floatval <4 and bust_floatval - waist_floatval >5:
        print("Hello dear your body type belongs to INVERTED TRIANGLE body shape")
        print("SUITABLE STYLE YOU LOOK BEST IN :: Wear soft-textured fabrics, A-line dresses, shirts with a tie "
              "below the bust line, tops that fall lower than the hip bone, tops with cuff sleeves, well-fitting "
              "clothes, V-necks, scoop tops, ruched t-shirts. For more info, click below link: ")
        print("https://www.makeupandbeautyblog.in/2020/10/how-to-dress-an-inverted-triangle-body-shape-a-style-guide.html")
        repeat()

    # For Rectangle
    if hip_floatval - bust_floatval < 3.6 and bust_floatval - hip_floatval < 3.6 and bust_floatval - waist_floatval < 9 and hip_floatval - waist_floatval < 10:
        print("Hello dear your body type belongs to RECTANGLE body shape")
        print("Your body size match to Rectangle body shape, "
              "SUITABLE STYLE YOU LOOK BEST IN :: Choose asymmetrical cuts to create "
              "curves. Pick skirts and dresses that are cinched at the waist. Opt for fitted, structured blazers and "
              "jackets. Look for straight, wide-legged and flared trousers and jeans (go high-waisted if you want a "
              "slim fit'). For more info, click below link:")
        print("https://styl-inc.com/blogs/how-to-style-a-rectangle-body-type-styl-inc-stylblog/")  # site URL
        img = Image.open('test.jpeg')  # image
        img.show()
        repeat()

    # For Diamond
    if waist_floatval - bust_floatval >= 1 and hip_floatval - bust_floatval < 2:
        print("Hello dear your body type belongs to Diamond shape, This body shape has a thicker waist circumference than the bust "
              "round or hip round.The stomach area may appear protruding. Some may call it an Apple when the upper "
              "body is slightly bigger than the hip."
              " SUITABLE STYLE YOU LOOK BEST IN :: you should dress in such a way to hide your "
              "tummy by jackets, dupattas or draping style dress. For more info, Click below link")
        print("https://www.ezibuy.com/shop/nz/find-your-body-shape/diamond-shape")
        repeat()

    #  FOR oval
    if bust_floatval - waist_floatval <= 0 and bust_floatval - hip_floatval > 1:
        print("Your body size match to OVAL body shape, Your waist is broader than your shoulders or hips. You’re "
              "generally well-proportioned. You have a fuller bust/upper body. Your waist is undefined. "
              "SUITABLE STYLE YOU LOOK BEST IN  :: Opt for silhouettes without structured waistlines to take focus away from the mid-section. "
              "Choose bust-defining tops in dark colours and diagonal/vertical stripes. Your Power Pieces: Go for a "
              "V-neck or a round neck and peplum tops. Pick high-waisted, slim fit and straight-leg trousers and "
              "jeans. Opt for high-waisted, pencil and A-line skirts. Choose imperial cut and strapless dresses. "
              "Bring in under-bust belts. For more info, Click below link:")
        print("https://effortlessstyleservices.com/how-to-dress-for-an-oval-body-shape/")
        repeat()'''


# repeat() asks user whether to continue or not
def repeat():
    repeat_val = input("Do you want to continue: Type Y or N: ")
    if repeat_val == 'Y' or repeat_val == 'y':
        figure_it_out()
    else:
        exit()


figure_it_out()

