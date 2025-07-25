import os
from PIL import Image
from multiprocessing import Pool, cpu_count
from functools import partial

# Compatibility for different Pillow versions
try:
    from PIL import ImageResampling
    RESAMPLE_MODE = ImageResampling.LANCZOS
except ImportError:
    RESAMPLE_MODE = Image.LANCZOS  # For Pillow < 10

# Config
input_dir = 'Demo/Tp'
output_dir = 'demo/Tp'
target_size = (1024, 1024)

os.makedirs(output_dir, exist_ok=True)

def resize_image(image_path, output_dir, target_size):
    try:
        img = Image.open(image_path)
        img = img.convert('RGB')
        img = img.resize(target_size, RESAMPLE_MODE)

        filename = os.path.basename(image_path)
        output_path = os.path.join(output_dir, filename)
        img.save(output_path, 'JPEG')
        print(f"Resized: {filename}")
    except Exception as e:
        print(f"Failed: {image_path} - {e}")

def main():
    image_paths = [
        os.path.join(input_dir, fname)
        for fname in os.listdir(input_dir)
        if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff'))
    ]

    print(f"Found {len(image_paths)} images.")
    with Pool(processes=cpu_count()) as pool:
        pool.map(partial(resize_image, output_dir=output_dir, target_size=target_size), image_paths)

if __name__ == '__main__':
    main()

# import os

# # Set your directories
# tp_dir = 'CASIA1.0/Tp'  # directory with images
# gt_dir = 'CASIA1.0/Gt'   # directory with masks

# # List all images and masks
# tp_images = sorted(os.listdir(tp_dir))
# gt_images = sorted(os.listdir(gt_dir))

# # Extract base names (without extension)
# tp_basenames = set(os.path.splitext(f)[0] for f in tp_images)
# gt_basenames = set(os.path.splitext(f)[0] for f in gt_images)

# # Count matches
# count_with_mask = 0
# count_without_mask = 0
# missing_images = []

# for basename in tp_basenames:
#     gt_name = basename + "_gt"
#     if gt_name in gt_basenames:
#         count_with_mask += 1
#     else:
#         count_without_mask += 1
#         missing_images.append(basename + '.jpg')

# print(f"Total TP images         : {len(tp_basenames)}")
# print(f"Total GT masks          : {len(gt_basenames)}")
# print(f"Images WITH masks       : {count_with_mask}")
# print(f"Images WITHOUT masks    : {count_without_mask}")

# if missing_images:
#     print("\nImages missing masks:")
#     for img in missing_images:
#         print(img)

# for img_name in missing_images:
#     img_path = os.path.join(tp_dir, img_name)
#     os.remove(img_path)
#     print(f"Deleted: {img_path}")

# import os
# import cv2

# # Set the folder path
# folder_path = 'CASIA1.0/Gt'

# # Supported image extensions
# image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp')

# # Create a list to store images
# images = []

# Loop through files in the folder
# for filename in os.listdir(folder_path):
#     if filename.lower().endswith(image_extensions):
#         original_path = os.path.join(folder_path, filename)

#         # Remove '_gt' from filename
#         new_filename = filename.replace('_gt', '')
#         new_path = os.path.join(folder_path, new_filename)

#         # Rename the file if needed
#         if filename != new_filename:
#             os.rename(original_path, new_path)
#             print(f"Renamed: {filename} -> {new_filename}")
#         else:
#             new_path = original_path  # No rename needed

#         # Read image
#         image = cv2.imread(new_path)
#         if image is not None:
#             images.append(image)
#         else:
#             print(f"Failed to read image: {new_filename}")

# print(f"\nTotal images successfully read: {len(images)}")

# import os
# from pathlib import Path

# # Set your directories
# image_dir = Path('CASIA1.0/Tp')
# mask_dir = Path('CASIA1.0/Gt')

# # Allowed image/mask extensions
# image_exts = ['.jpg', '.jpeg', '.png', '.bmp']
# mask_exts = ['.jpg', '.jpeg', '.png', '.bmp']

# # Build mappings: {stem -> full_path}
# image_files = {f.stem: f for ext in image_exts for f in image_dir.glob(f'*{ext}')}
# mask_files = {f.stem: f for ext in mask_exts for f in mask_dir.glob(f'*{ext}')}

# # Delete masks without corresponding image
# for name, path in mask_files.items():
#     if name not in image_files:
#         print(f"Removing unmatched mask: {path}")
#         path.unlink()

# # Delete images without corresponding mask
# for name, path in image_files.items():
#     if name not in mask_files:
#         print(f"Removing unmatched image: {path}")
#         path.unlink()
