import sys
from PIL import Image


def create_square_image(image):
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


def main(args):
    if '-s' in args:
        image_file = args[
            args.index('-s') + 1
        ]

        image = create_square_image(
            Image.open(image_file)
        )

        file_name, file_ext = image_file.rsplit('.', 1)
        file_name += "_sqaure_"
        image.save(file_name + '.' + file_ext)


if __name__ == "__main__":
    main(sys.argv)
