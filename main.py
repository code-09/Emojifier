import argparse

# import json
# import requests
# from pixel_processor import convert_image_to_string, convert_image_to_emoji_list
# from image_processor import create_opencv_image_from_url
# from typing import *
# import numpy as np
# import cv2


# def emojify():
#     width = 50
#     height = 50
#     emoji_width = 50
#     emoji_height = 50

#     image = create_opencv_image_from_url(bytearray(req.content), width, height)
#     emojis = convert_image_to_emoji_list(image)

#     loaded_images = {}
#     complete_image = None
#     for row in emojis:
#         row_image = None
#         for emoji in row:
#             if emoji not in loaded_images:
#                 image = cv2.imread(f"/svgs/{emoji}.svg.png", cv2.IMREAD_COLOR)
#                 loaded_images[emoji] = cv2.resize(
#                     image, (emoji_width, emoji_height), interpolation=cv2.INTER_AREA
#                 )

#             # Now we know we're in the cache
#             if row_image is None:
#                 row_image = loaded_images[emoji]
#             else:
#                 row_image = np.hstack((row_image, loaded_images[emoji]))
#         if complete_image is None:
#             complete_image = row_image
#         else:
#             complete_image = np.vstack((complete_image, row_image))

#     success, encoded_image = cv2.imencode(".png", complete_image)
#     image_bytes = encoded_image.tobytes()


def main():
    parser = argparse.ArgumentParser(
        description="Takes an input image, and creates a replica of the image using nothing but emojis."
    )

    parser.add_argument(
        "--width",
        type=int,
        default=50,
        help="width of output image (Default: 50 emojis)",
    )

    parser.add_argument(
        "--height",
        type=int,
        default=50,
        help="height of output image (Default: 50 emojis)",
    )

    parser.add_argument(
        "--input_image",
        required=True,
        help="path to the image to convert, supports png and jpg",
    )

    parser.add_argument(
        "--output_file", help="path to store the output. Outputs in png format.",
    )

    args = parser.parse_args()

    print(f"{args.height}x{args.width} {args.input_image} {args.output_file}")


if __name__ == "__main__":
    main()
