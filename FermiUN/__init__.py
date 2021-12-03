from munch import Munch
import yaml 

class FermiUN(object):
    # Import Methods from Files
    from ._create_config_file import create_config_file
    # TODO: Add plotting methods
    # One for plotting the current loss curve that is called during training after an epoch
    # One for plotting a nice summary over the trained model with some example images and performance
    # TODO: Inference functions that take a single image or a batch and predict the central area
    # These should likely just save the resulting predicted image in a format defined in the config.
    
    # Default constructor, will likely disable later
    def __init__(self):
        self.config = None
        self.configpath = ""
        self.modelhandler = None
        self.datahandler = None

    @classmethod
    def from_saved_model(cls, modelpath : str, configpath : str):
        '''
        Loads a previously trained model to analyze images.
        :param modelpath: Filepath of the saved model
        :param configpath: Filepath of the config file
        '''
        pass

    @classmethod
    def from_configfile(cls, configpath : str):
        '''
        Sets up a model for training according to its config file
        :param configpath: Filepath of the config file
        '''
        obj = cls()
        obj.load_config_file(configpath)
        return obj

    @classmethod
    def autotrain(cls, folderpath : str, configpath : str):
        '''
        Sets up and trains a model automatically.
        :param folderpath: Filepath of the folder with cropped training data
        :param configpath: Filepath of the config file
        '''
        pass

    def load_config_file(self, path : str):
        '''
        Load a new config file.
        :param path: Filepath of the config file.
        '''
        with open(path, "r") as conf_file:
            file_content = conf_file.read()
            self.config = Munch.fromYAML(file_content)
            self.configpath = path

    