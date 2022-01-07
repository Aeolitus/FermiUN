from munch import Munch
from FermiUN.ModelHandler import ModelHandler
from FermiUN.DataHandler import DataHandler
import yaml 
import numpy as np
import tensorflow
from tensorflow.keras.models import load_model
from os.path import join

class FermiUN(object):
    # Import Methods from Files
    from ._create_config_file import create_config_file
    
    def __init__(self, configpath : str):
        self.config = None
        self.load_config_file(configpath)
        self.configpath = "configpath"
        self.mask = self.generate_mask()
        self.modelhandler = ModelHandler(self.config, self.mask)
        self.datahandler = DataHandler(self.config, self.mask)

        physical_devices = tensorflow.config.list_physical_devices('GPU')
        tensorflow.config.experimental.set_memory_growth(physical_devices[0], True)

    @classmethod
    def from_saved_model(cls, modelpath : str, configpath : str):
        '''
        Loads a previously trained model to analyze images.
        :param modelpath: Filepath of the saved model
        :param configpath: Filepath of the config file
        '''
        obj = cls.from_configfile(configpath)
        obj.load_model(modelpath)
        return obj

    @classmethod
    def from_configfile(cls, configpath : str):
        '''
        Sets up a model for training according to its config file
        :param configpath: Filepath of the config file
        '''
        obj = cls()
        obj.load_config_file(configpath)
        return obj

    # Is this kind of class constructor a good idea?
    @classmethod
    def autotrain(cls, configpath : str):
        '''
        Sets up and trains a model automatically.
        :param configpath: Filepath of the config file
        '''
        obj = cls()
        obj.load_config_file(configpath)
        obj.initialize_for_training()
        obj.train()
        return obj

    def load_config_file(self, path : str):
        '''
        Load a new config file.
        :param path: Filepath of the config file.
        '''
        with open(path, "r") as conf_file:
            file_content = conf_file.read()
            self.config = Munch.fromYAML(file_content)
            self.configpath = path

    def save_config_file_as(self, path : str):
        '''
        Save the config file to a new location.
        :param path: Filepath of the config file to save into
        '''
        with open(path, "w") as conf_file:
            conf_file.write(self.config.toYAML())

    def save_config_file(self):
        '''
        Save changes to the current config file.
        '''
        self.save_config_file_as(self.configpath)

    def import_images(self, folderpath : str, imagename : str):
        '''
        Import, crop and rescale images from a folder.
        :param folderpath: Folder from which images are imported. Can be a list of folders.
        :param imagename: Name of the images (must appear in the filename)
        '''
        print("Importing images into the imagefolder...")
        if isinstance(folderpath, str):
            self.datahandler.crop_and_copy_from_folder(folderpath, imagename)
        else:
            totalnum = len(folderpath)
            i = 1
            for path in folderpath:
                print(f"Loading folder {i} out of {totalnum}...")
                self.datahandler.crop_and_copy_from_folder(path, imagename)
                i = i + 1
        self.save_config_file()

    def generate_mask(self) -> np.array:
        '''
        Creates a binary mask as defined in the config file with the central area zeroed out.
        :return mask: The two-dimensional np.array with the same size as the images. 
        '''
        scale = np.arange(self.config.image.width)
        mask = np.zeros((self.config.image.width, self.config.image.width))
        
        mask[(scale[np.newaxis, :] - (self.config.image.width - 1) / 2) ** 2 \
            + (scale[:, np.newaxis] - (self.config.image.width - 1) / 2) ** 2 \
            > self.config.radius ** 2] = 1

        return mask

    def save_model(self, filepath : str):
        '''
        Saves the current model and loss history 
        :param filepath: Path to the model file
        '''
        if filepath[-3:] != ".h5":
            filepath = filepath + ".h5"
        self.modelhandler.model.save(filepath)

    def load_model(self, modelpath : str):
        '''
        Loads a given model.
        :param modelpath: Filepath to the saved model
        '''
        self.modelhandler.model = load_model(modelpath)

    def initialize_for_training(self):
        '''
        Initializes a model from scratch.
        '''
        self.datahandler.make_train_validation_test_split()
        self.save_config_file_as(join(self.config.imagefolder, "config.yaml"))
        self.modelhandler.init_model()

    def train(self):
        '''
        Trains the model on the data stored in the imagefolder.
        '''
        self.modelhandler.train_model()
        
    