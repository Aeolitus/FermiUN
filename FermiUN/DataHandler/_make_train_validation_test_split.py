import numpy as np
from os import listdir
from os.path import basename

def make_train_validation_test_split(self):
    '''
    Splits the files in the imagefolder into the three categories.
    '''
    # Filter out other files that might be in the folder, but arent data
    imagefolder_contents = [el for el in listdir(self.config.imagefolder) \
        if self.config.imageprefix in basename(el) and '.npy' in basename(el)]

    indices = np.arange(len(imagefolder_contents))
    np.random.shuffle(indices)
    
    index_test_end = int(self.config.test_fraction * len(imagefolder_contents))
    index_validation_end = index_test_end + int(self.config.validation_fraction * len(imagefolder_contents))

    self.config.testlist = indices[0:index_test_end]
    self.config.validationlist = indices[index_test_end+1:index_validation_end]
    self.config.trainlist = indices[index_validation_end+1:]
    