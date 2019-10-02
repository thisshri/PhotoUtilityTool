import sys
from PIL import Image, ImageOps, ImageDraw

def create_square_image(image):
    padding = round(
        abs(image.width - image.height) / 2
    )

    top = right = bottom = left = 0
    if image.height > image.width:
        left = right = padding
    else :
        top = bottom = padding

    width = left + image.size[0] + right
    height = top + image.size[1] + bottom
    square_image = Image.new(image.mode, (width, height), color=(255, 255, 255))
    square_image.paste(image, (left, top))

def main(*args, **kwargs):
    print(args)
    print(kwargs)

    image = Image.open('foo.jpg')
    image = create_square_image(image)
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    sys.argv

    kwargs = sys.argv[2:]
    iter_kwargs = iter(kwargs)
    # way to specify wheather a file or folder is passed, FLAG
    main(sys.argv, kwargs)
