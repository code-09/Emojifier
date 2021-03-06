"""
Contains helper functions for processing
images and converting them to emojis
"""
from typing import *
from emoji_mappings import color_dictionary as curr_emoji_dict
import itertools


def to_four_bit(color_input: Tuple[int, int, int]) -> Tuple[int, int, int]:
    r, g, b = color_input
    r = r * 16 // 255
    g = g * 16 // 255
    b = b * 16 // 255
    if r == 16:
        r -= 1
    if g == 16:
        g -= 1
    if b == 16:
        b -= 1
    return (r, g, b)


def to_eight_bit(color_input: Tuple[int, int, int]) -> Tuple[int, int, int]:
    r, g, b = color_input
    r = r * 255 // 16
    g = g * 255 // 16
    b = b * 255 // 16
    return (r, g, b)


def get_closest_key_eight_bit(
    rgb: Tuple[int, int, int], color_dictionary: Dict[Tuple[int, int, int], str]
) -> Tuple[int, int, int]:
    """
    Iterates over the keys in the dictionary, returns closest key
    """
    red, green, blue = rgb
    smallest_distance = 1000000  # Larger than max smallest distance
    r = 0
    g = 0
    b = 0
    for k in color_dictionary.keys():
        diff_red = abs(k[0] - red) ** 2
        diff_green = abs(k[1] - green) ** 2
        diff_blue = abs(k[2] - blue) ** 2
        summation = diff_red + diff_green + diff_blue
        if summation < smallest_distance:
            smallest_distance = summation
            r, g, b = k

    return (r, g, b)


def convert_image_to_string(image):
    to_return = ""
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            red: int = image[i][j][0]
            green: int = image[i][j][1]
            blue: int = image[i][j][2]
            to_return += f"{color_dict[to_four_bit((red, green, blue))]}"
        to_return += "|"

    return to_return


def convert_image_to_emoji_list(image):
    to_return = []
    for i in range(image.shape[0]):
        row = []
        for j in range(image.shape[1]):
            red: int = image[i][j][0]
            green: int = image[i][j][1]
            blue: int = image[i][j][2]
            emoji_name = color_dict[to_four_bit((red, green, blue))]
            row.append(emoji_name.replace(":", ""))
        to_return.append(row)

    return to_return


color_dict = {}
for r in range(16):
    for g in range(16):
        for b in range(16):
            eight_bit_rgb = to_eight_bit((r, g, b))
            closest_key = get_closest_key_eight_bit(eight_bit_rgb, curr_emoji_dict)
            color_dict[(r, g, b)] = curr_emoji_dict[closest_key]
