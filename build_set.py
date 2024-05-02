import os
import argparse
from adjust import resize_and_darken_image

def process_images(input_dir, output_dir, brightness):
    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over all files in the input directory
    for filename in os.listdir(input_dir):
        # Construct the full file path
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Check if the file is an image (optional, based on file extension)
        if input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            # Process the image
            resize_and_darken_image(input_path, output_path, size=(224, 224), darken_factor=brightness)
        else:
            print(f"Skipped non-image file: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Batch process images to adjust size and brightness.")
    parser.add_argument('--input_dir', type=str, default="/Users/aidan/Documents/COS484/nlp_clipscore/example/raw_images",
                        help="Directory containing the raw images")
    parser.add_argument('--output_dir', type=str, default="/Users/aidan/Documents/COS484/nlp_clipscore/example/testset/b-100",
                        help="Directory to save the adjusted images")
    parser.add_argument('--brightness', type=float, default=1.0,
                        help="Brightness factor to adjust the image (less than 1 to darken, more than 1 to brighten)")

    args = parser.parse_args()

    process_images(args.input_dir, args.output_dir, args.brightness)

if __name__ == '__main__':
    main()
