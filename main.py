from Package_figure_it_out.Functions_figure_it_out import *
from PIL import Image


def main():
    input_val = validate()
    convert_val = convert_str_float(input_val[0], input_val[1], input_val[2], input_val[3])
    final_val = find_body_type(convert_val[0], convert_val[1], convert_val[2], convert_val[3])
    # print(type(val_input))
    # print(type(val_convert))
    # print(type(val_final))
    if type(final_val) == tuple:
        print(f"Your body type is :{final_val[0]}")
        print(f"Description: {final_val[2]}")
        print(f"Click this link for more info: {final_val[3]}")
        img = Image.open(final_val[1])  # image
        img.show()
    else:
        print(final_val)

    str_repeat = repeat()
    if str_repeat == 'Y' or str_repeat == 'y':
        main()
    else:
        exit()


main()


