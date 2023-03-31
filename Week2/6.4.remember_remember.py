import math
import matplotlib.image as mpimg

def round_number(*number):
    '''
    Round the number to 2 decimal places
    :param number:
    :return: the number rounded to 2 decimal places
    '''
    return [float('{:.2f}'.format(num)) for num in number]


def decode_image(filename):
    '''
    Decode the image and return the message
    :param filename: the name of the image file
    :return:    the message encoded in the image
    '''
    # Load the image
    img = mpimg.imread(filename)
    height, width, _ = img.shape
    # Loop through each column and find the black pixel
    positions = []
    for x in range(width):
        for y in range(height):
            r, g, b, _ = img[y, x]
            r, g, b = round_number(r, g, b)
            if r == 0 and g == 0 and b == 0:
                positions.append(y)
                break
    # Convert the positions to characters and return the message
    message = ''.join(chr(pos) for pos in positions)
    return message

# test function
print(decode_image("../resources/code.png"))