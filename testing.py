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

