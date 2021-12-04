from os import listdir, mkdir
from os.path import join, exists
import numpy as np
from skimage.io import imread
from tqdm import tqdm

def read_crop_and_cap(self, imagepath : str) -> np.array:
    top = int(self.config.image.center_y-self.config.image.width/2.0)
    left = int(self.config.image.center_x-self.config.image.width/2.0)
    if top < 0 or left < 0:
        raise Exception("Crop window exceeds image bounds.")

    img = imread(imagepath)
    img = img[top : top + self.config.image.width, \
        left : left + self.config.image.width]

    # Rescale and cut of outliers - 4x the average seems pretty reasonable
    magnitude = (4 * np.average(img))
    if magnitude < 400:
        print(f"Found an image with no light on bright - Path: {imagepath}")
    img = img / magnitude 
    img[img > 1.0] = 1.0   # Sometimes there are hot pixels that need to be cut
    img[img < 0.0] = 0.0   # Should never occur, cant count negative numbers of photons

    return img

    

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

    img_list = [join(folderpath, el) for el in listdir(folderpath) if imagename in el]
    old_img_number = len(listdir(target_folder))
    img_number = old_img_number

    for img in tqdm(img_list):
        try:
            img = self.read_crop_and_cap(img)
            target_name = target_folder + '/' + self.config.imageprefix + str(img_number)
            np.save(target_name, img)
            img_number = img_number + 1
        except Exception: 
            pass
    
    print(f"{img_number-old_img_number} images were imported, for a total of {img_number}.")