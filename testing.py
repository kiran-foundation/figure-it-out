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


# figure_it_out() returns dictionary

def find_body_type(bust, waist, hip, high_hip):
    bust_hip = bust - hip
    bust_waist = bust - waist
    hip_bust = hip - bust
    hip_waist = hip - waist
    if hip_bust < 1.5 and hip_bust > 0  and hip_waist == 8 or hip_bust < 1.5 and hip_bust >0 and hip_waist == 7:
        return body_type_dict['ideal_figure'], body_type_image_dict['ideal_figure'], body_type_desc_dict['ideal_figure'],body_type_URL_dict['ideal_figure']
    if bust_hip <= 2 and bust_hip > 0 and bust_waist >= 8 or hip_bust <= 2 and hip_bust > 0 and hip_waist >= 8:
        return body_type_dict['hourglasse'],body_type_image_dict['hourglasse'],body_type_desc_dict['hourglasse'],body_type_URL_dict['hourglasse']
    if hip_bust >= 3 and hip_waist >= 8 and bust_waist > 0 and hip-high_hip <= 5:
        return body_type_dict['spoon'],body_type_image_dict['spoon'],body_type_desc_dict['spoon'],body_type_URL_dict['spoon']
    if hip_bust >= 3 and hip_waist >= 8 and bust_waist > 0 and hip-high_hip > 5:
        return body_type_dict['triangle'], body_type_image_dict['triangle'], body_type_desc_dict['triangle'], body_type_URL_dict['triangle']
    if bust_hip > 1 and hip_bust < 0  and bust_waist >= 5:
        return body_type_dict['inverted_triangle'],body_type_image_dict['inverted_triangle'],body_type_desc_dict['inverted_triangle'],body_type_URL_dict['inverted_triangle']
    if hip_bust <= 3 and  hip_bust >0 and bust_waist < 3 and bust_waist >0 or  hip_bust <= 3 and hip_bust >= 0 and bust_hip < 3 and bust_hip >0:
        return body_type_dict['rectangle'],body_type_image_dict['rectangle'],body_type_desc_dict['rectangle'],body_type_URL_dict['rectangle']
    if bust_waist <= 0  and hip_waist <= 0 and hip_bust <= 3 and hip_bust >=0 or bust_waist <= 0  and hip_waist <= 0 and bust_hip <= 3 and bust_hip >0:
        return body_type_dict['diamond'],body_type_image_dict['diamond'],body_type_desc_dict['diamond'],body_type_URL_dict['diamond']
    if hip_waist <=2  and hip_bust >= 2   or bust_hip >=1 and bust_waist<=0:
        return body_type_dict['oval'],body_type_image_dict['oval'],body_type_desc_dict['oval'],body_type_URL_dict['oval']
    else:
        return "Invalid Measurements"
