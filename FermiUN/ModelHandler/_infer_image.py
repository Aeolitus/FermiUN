import numpy as np
from skimage.io import imread
from FermiUN.DataHandler._crop_and_copy_from_folder import read_crop_and_cap
from FermiUN.ModelHandler._create_batch import mask_image

def infer_image(self, imagepath : str): #  -> tuple[np.array, np.array, np.array]
    '''
    Given a path to an image, evaluate the model on it
    :param imagepath: Path to the image file
    :return: masked image, predicted image, true image
    '''
    img = self.read_crop_and_cap(imagepath)
    X, Y = self.mask_image(img)

    prediction = self.model.predict(X[np.newaxis, :, :])
    prediction = prediction[0,:,:]

    return X, prediction, Y