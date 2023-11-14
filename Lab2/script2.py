import os
import shutil
import csv
import logging
from typing import List

logging.basicConfig(filename='annotation2.log', level=logging.INFO)

def get_paths2(name: str) -> tuple[list[str], list[str]]:
    """
    This function returns a tuple of absolute and relative paths for all images
    of the specific name of the animal passed to the function,
    after moving the images to another directory.
    """
    absolute_path = os.path.abspath(os.path.join('dataset2', name))
    image_paths = [os.path.join(absolute_path, img) for img in os.listdir(absolute_path)]

    relative_path = os.path.relpath(os.path.join('dataset2', name))
    relative_paths = [os.path.join(relative_path, img) for img in os.listdir(relative_path)]

    return image_paths, relative_paths

def replace_images2(name: str) -> None:
    """
    This function changes the names of images by combining the image number and class
    in the format class_number.jpg,
    transfers the images to the dataset2 directory, and deletes the folder
    where the class images were stored.
    """
    relative_path = os.path.relpath('dataset2')
    class_path = os.path.join(relative_path, name)
    image_names = os.listdir(class_path)

    image_relative_paths = [os.path.join(class_path, img) for img in image_names]
    new_img_relative_paths = [os.path.join(relative_path, f'{name}_{img}') for img in image_names]

    for old_name, new_name in zip(image_relative_paths, new_img_relative_paths):
        os.replace(old_name, new_name)

    os.chdir('dataset2')
    if os.path.isdir(name):
        os.rmdir(name)
    os.chdir('..')

def main() -> None:
    cat, dog = 'cat', 'dog'
    if os.path.isdir('dataset2'):
        shutil.rmtree('dataset2')
    old = os.path.relpath('dataset')
    new = os.path.relpath('dataset2')
    shutil.copytree(old, new)

    replace_images2(cat)
    replace_images2(dog)

    cat_absolute_paths, cat_relative_paths = get_paths2(cat)
    dog_absolute_paths, dog_relative_paths = get_paths2(dog)

    with open('annotation2.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', lineterminator='\r')

        for absolute_path, relative_path, label in zip(cat_absolute_paths, cat_relative_paths, [cat] * len(cat_absolute_paths)):
            writer.writerow([absolute_path, relative_path, label])
            logging.info(f"Added entry for {label}: {absolute_path}")

        for absolute_path, relative_path, label in zip(dog_absolute_paths, dog_relative_paths, [dog] * len(dog_absolute_paths)):
            writer.writerow([absolute_path, relative_path, label])
            logging.info(f"Added entry for {label}: {absolute_path}")

if __name__ == "__main__":
    main()
