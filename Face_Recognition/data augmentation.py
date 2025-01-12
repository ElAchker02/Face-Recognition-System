from imgaug import augmenters as iaa
import cv2
import os
import numpy as np

class DataAugmentation:
    def __init__(self, save_dir, target_size=(160, 160)):
        self.save_dir = save_dir
        self.target_size = target_size
        self.augmenters = iaa.Sequential([
            iaa.Fliplr(0.5),  # Horizontal flip with 50% probability
            iaa.Affine(rotate=(-10, 10), scale=(0.9, 1.1)),  # Random rotation and scaling
            iaa.AdditiveGaussianNoise(scale=(0, 0.02 * 255)),  # Gaussian noise
            iaa.Multiply((0.8, 1.2)),  # Random brightness
            iaa.GaussianBlur(sigma=(0, 1.0))  # Blurring
        ])

    def augment_image(self, img):
        # Ensure the image is in RGB format
        if len(img.shape) == 3 and img.shape[-1] == 3:
            img_rgb = img
        else:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Generate multiple augmented versions of the image
        augmented_images = self.augmenters.augment_images([img_rgb] * 5)  # 5 augmentations
        return augmented_images

    def augment_folder(self, input_dir):
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        for sub_dir in os.listdir(input_dir):
            class_dir = os.path.join(input_dir, sub_dir)
            save_class_dir = os.path.join(self.save_dir, sub_dir)

            if not os.path.exists(save_class_dir):
                os.makedirs(save_class_dir)

            # Loop through image files
            for img_name in os.listdir(class_dir):
                if img_name.lower().endswith(('.jpg', '.jpeg')):  # Handle jpg and jpeg formats
                    img_path = os.path.join(class_dir, img_name)
                    img = cv2.imread(img_path)

                    if img is not None:
                        # Augment the image
                        augmented_images = self.augment_image(img)
                        for idx, aug_img in enumerate(augmented_images):
                            # Save augmented images
                            save_path = os.path.join(save_class_dir, f"{img_name.split('.')[0]}_aug{idx}.jpg")
                            cv2.imwrite(save_path, cv2.cvtColor(aug_img, cv2.COLOR_RGB2BGR))
            print(f"Augmented images saved for class: {sub_dir}")

# Define paths
input_directory = "dataset"
augmented_directory = "augmented_dataset"

# Perform augmentation
augmenter = DataAugmentation(save_dir=augmented_directory)
augmenter.augment_folder(input_directory)
