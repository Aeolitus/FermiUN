from os import listdir, mkdir, makedirs
from os.path import join, exists, isdir
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
    makedirs(target_folder, exist_ok=True)

    img_list = [join(folderpath, el) for el in listdir(folderpath) if imagename in el]

    folder_nums = [int(el.removeprefix("images_")) for el in listdir(target_folder) \
        if isdir(join(target_folder, el)) and "images_" in el]
    folder_nums.append(0)
    current_folder = join(target_folder, "images_" + str(max(folder_nums)))
    makedirs(current_folder, exist_ok=True)
    image_nums = [int(el.removesuffix(".npy").removeprefix(self.config.imageprefix)) \
        for el in listdir(current_folder) if ".npy" in el]
    if len(image_nums) == 0:
        old_img_number = max(folder_nums)*10000
    else:
        old_img_number = max(image_nums)+1
    img_number = old_img_number

    for img in tqdm(img_list):
        if img_number >= (max(folder_nums)+1)*10000:
            folder_nums.append(max(folder_nums)+1)
            current_folder = join(target_folder, "images_" + str(max(folder_nums)))
            makedirs(current_folder, exist_ok=True)

        try:
            img = self.read_crop_and_cap(img)
            target_name = join(current_folder, self.config.imageprefix + str(img_number) + ".npy")
            np.save(target_name, img)
            self.config.filelist.append(target_name)
            img_number = img_number + 1

        except Exception: 
            print(f"There was an exception caught for image number {img_number}, skipped.")
    
    print(f"{img_number-old_img_number} images were imported, for a total of {img_number}.")