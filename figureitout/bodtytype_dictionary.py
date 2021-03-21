def find_body_type(bust, waist, hip, high_hip):
    if bust - hip <= 1 and hip - bust <= 3.6 and bust - waist >= 9 or hip - waist >= 10:
        return "hourglasse"
    if hip - bust >= 4 and hip - waist< 9:
        return "spoon"
    if hip - bust>= 3 and bust - waist< 6:
        return "triangle"
    if bust - hip < 4 and bust - waist > 5:
        return "inverted triangle"
    if hip - bust < 3.6 and bust - hip < 3.6 and bust- waist < 9 and hip - waist< 10:
        return "rectangle"
    if waist - bust>= 1 and hip - bust < 2:
        return "diamond"
    if bust - waist<= 0 and bust- hip > 1:
        return "oval"

