from fio.resources import *


# figure_it_out() returns dictionary

def find_body_type(bust, waist, hip, high_hip):
    bust_hip = bust - hip
    bust_waist = bust - waist
    hip_bust = hip - bust
    hip_waist = hip - waist
    if hip_bust == 1.5 and hip_waist == 8 or hip_bust == 1.5 and hip_waist == 7:
        return body_type_dict['ideal_figure'], body_type_image_dict['ideal_figure'], body_type_desc_dict[
            'ideal_figure'], body_type_URL_dict['ideal_figure']
    if bust_hip <= 2 and bust_hip > 0 and bust_waist >= 5 or hip_bust <= 2 and hip_bust > 0 and hip_waist >= 5 :
        return body_type_dict['hourglasse'], body_type_image_dict['hourglasse'], body_type_desc_dict['hourglasse'], \
               body_type_URL_dict['hourglasse']
    if hip_bust >= 3 and hip_waist >= 4  and hip - high_hip <= 4 :
        return body_type_dict['spoon'], body_type_image_dict['spoon'], body_type_desc_dict['spoon'], body_type_URL_dict[
            'spoon']
    if hip_bust >= 3 and hip_waist > 0 and hip - high_hip > 4:
        return body_type_dict['triangle'], body_type_image_dict['triangle'], body_type_desc_dict['triangle'], \
               body_type_URL_dict['triangle']
    if bust_hip > 1 and hip_bust < 0 and bust_waist >= 5:
        return body_type_dict['inverted_triangle'], body_type_image_dict['inverted_triangle'], body_type_desc_dict[
            'inverted_triangle'], body_type_URL_dict['inverted_triangle']
    if hip_bust <= 3 and hip_bust > 0 and hip_waist <= 4 and hip_waist >= 0 or bust_waist <= 4 and bust_hip >= 0 and bust_hip <= 4 and bust_hip > 0:
        return body_type_dict['rectangle'], body_type_image_dict['rectangle'], body_type_desc_dict['rectangle'], \
               body_type_URL_dict['rectangle']
    if bust_waist < 0 and hip_waist < 0 and hip_bust <= 3 and hip_bust > 0 or bust_waist < 0 and hip_waist < 0 and bust_hip <= 3 and bust_hip > 0:
        return body_type_dict['diamond'], body_type_image_dict['diamond'], body_type_desc_dict['diamond'], \
               body_type_URL_dict['diamond']
    if hip > bust and waist > bust and hip <= waist or hip < bust and waist > hip and bust <= waist:
        return body_type_dict['oval'], body_type_image_dict['oval'], body_type_desc_dict['oval'], body_type_URL_dict[
            'oval']
    else:
        return "Invalid Measurements"


#  Function returns images list based on body type
def body_type_images(bodytype):
    body_type_images_list = []
    if bodytype == 'IDEAL FIGURE':
        body_type_images_list = list(ideal_image_list)  # Copies images from one list to other list
    if bodytype == 'HOURGLASSE':
        body_type_images_list = list(hourglass_image_list)
    if bodytype == 'SPOON':
        body_type_images_list = list(spoon_image_list)
    if bodytype == 'TRIANGLE':
        body_type_images_list = list(triangle_image_list)
    if bodytype == 'INVERTED TRIANGLE':
        body_type_images_list = list(inverted_triangle_image_list)
    if bodytype == 'RECTANGLE':
        body_type_images_list = list(rectangle_image_list)
    if bodytype == 'DIAMOND':
        body_type_images_list = list(diamond_image_list)
    if bodytype == 'OVAL':
        body_type_images_list = list(oval_image_list)

    return body_type_images_list
