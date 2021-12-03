from munch import Munch
import yaml

@classmethod
def create_config_file(cls, path : str):
    conf = Munch() # Dict with dot notation for readability
    # TODO: Replace default values
    conf.image = Munch()
    conf.image.width = 200
    conf.image.center_x = 100
    conf.image.center_y = 100
    conf.radius = 50
    conf.imagefolder = "L:/FermiUN_TrainingData"
    conf.imageprefix = "bright_"
    conf.testlist = []
    conf.trainlist = []
    conf.validationlist = []
    conf.model_path = ""
    conf.validation_fraction = 0.2
    conf.test_fraction = 0.1
    conf.batch_size = 8
    conf.learning_rate = 5e-6
    conf.max_epochs = 1000

    with open(path, "w") as conf_file:
        conf_file.write(conf.toYAML())
    