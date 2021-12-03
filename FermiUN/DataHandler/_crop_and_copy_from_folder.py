from os import listdir, mkdir
from os.path import join, exists
import numpy as np
from skimage.io import imread
from tqdm import tqdm

def crop_and_copy_from_folder(self, folderpath : str, imagename : str):
    '''
    Takes all images in a folder where the filename contains a certain word,
    crops them and saves the cropped image to the imagefolder given in the 
    configuration file.
    :param folderpath: The folder from which images are taken
    :param imagename: String that appears in the filename to match. 
    '''
    if not exists(folderpath):
        raise Exception("Source imagefolder does not exist.")

    target_folder = self.config.imagefolder
    if not exists(target_folder):
        mkdir(target_folder)

    top = int(self.config.image.center_y-self.config.image.width/2.0)
    left = int(self.config.image.center_x-self.config.image.width/2.0)
    if top < 0 or left < 0:
        raise Exception("Crop window exceeds image bounds.")

    img_list = [join(folderpath, el) for el in listdir(folderpath) if imagename in el]
    old_img_number = len(listdir(target_folder))
    img_number = old_img_number
    for img in tqdm(img_list):
        img = imread(img)
        img = img[top : top + self.config.image.width, \
            left : left + self.config.image.width]

        # Rescale and cut of outliers
        # TODO: This should probably be automatically determined from the images
        img = img / self.config.image.max_value
        img[img > 1.0] = 1.0 # TODO: Should this be somehow marked as an outlier?
        img[img < 0.0] = 0

        target_name = target_folder + '/' + self.config.imageprefix + str(img_number)
        np.save(target_name, img)
        img_number = img_number + 1
    print(f"{img_number-old_img_number} images were imported, for a total of {img_number}.")