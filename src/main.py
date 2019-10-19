#!/bin/python3

from PIL import Image
from argparse import ArgumentParser


def create_square_image(image):
    """
    Create new image with 1:1 aspect ration by adding white padding to the
    required sides of images.
    """
    padding = round(
        abs(image.width - image.height) / 2
    )

    top = right = bottom = left = 0
    if image.height > image.width:
        left = right = padding
    else:
        top = bottom = padding

    width = left + image.size[0] + right
    height = top + image.size[1] + bottom
    square_image = Image.new(
        image.mode,
        (width, height),
        color=(255, 255, 255)
        )
    square_image.paste(image, (left, top))
    return square_image


def main():
    parser = ArgumentParser(
        description='Create new image with aspect ration 1:1 by padding it' +
        ' with white background'
    )

    parser.add_argument(
        '--i',
        metavar='IMAGE_FILE(S)',
        nargs='*',
        type=str,
        required=True,
        dest='image_files',
        help='Path of image file(s).'
    )

    for image_file in parser.parse_args().image_files:
        image = create_square_image(
            Image.open(image_file)
        )

        file_name, file_ext = image_file.rsplit('.', 1)
        file_name += "_sqaure_"
        image.save(file_name + '.' + file_ext)


if __name__ == "__main__":
    main()
