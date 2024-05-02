import argparse
from PIL import Image, ImageEnhance

def resize_and_darken_image(input_path, output_path, size, darken_factor):
    # Open the image file
    img = Image.open(input_path)

    # Optionally darken the image
    if darken_factor is not None:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(darken_factor)

    # Resize the image
    img = img.resize(size, Image.LANCZOS)
    # Save the resized image
    img.save(output_path)

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Resize an image to a specified size.')
    parser.add_argument('input_path', type=str, help='The file path to the input image.')
    parser.add_argument('output_path', type=str, help='The file path for the output image.')
    parser.add_argument('--width', type=int, default=224, help='Width of the resized image.')
    parser.add_argument('--height', type=int, default=224, help='Height of the resized image.')
    parser.add_argument('--darken', type=float, default=1.0, help='Darken the image by this factor (less than 1 to darken, 1 to keep unchanged)')

    # Parse the arguments
    args = parser.parse_args()

    # Define the size tuple
    size = (args.width, args.height)

    # Call the resize image function
    resize_and_darken_image(args.input_path, args.output_path, size, args.darken)

if __name__ == '__main__':
    main()
