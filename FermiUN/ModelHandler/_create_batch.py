import numpy as np
from skimage.io import imread

def mask_image(self, image : np.array) -> tuple[np.array]:
    '''
    Takes an image and returns it masked as well as the original
    :param image: Input image
    :returns: Masked image, Original Image
    '''

    left = int(self.config.image.width / 2 - self.config.radius)
    right = int(self.config.image.width / 2 + self.config.radius)

    Y = image[left:right, left:right] # what the network should ideally predict
    temp = image * self.mask
    X = temp + (1 - self.mask) * 0.5 # set image to 0.5 where the mask is

    return X, Y


def create_batch(self, list_of_files : list[str], list_of_indices : list[int]) -> tuple[np.array, np.array]:
    '''
    Creates a batch of masked images and associated targets.
    :param list_of_files: is a list of all images in the imagefolder
    :param list_of_indices: is a list of indices in that list which should be used.
    '''
    X = np.empty([len(list_of_indices), self.config.image.width, self.config.image.width])
    Y = np.empty([len(list_of_indices), self.config.radius*2, self.config.radius*2])

    for i in range(len(list_of_indices)):
        img = np.load(list_of_files[i])
        X[i,:,:], Y[i,:,:] = self.mask_image(img)

    return X, Y