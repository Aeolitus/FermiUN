__all__ = ["_define_model", "_init_model", "_train_model"]

class ModelHandler(object): 
    # Import Methods from Files
    from ._define_model import define_model
    from ._init_model import init_model
    from ._train_model import train_model
    from ._create_batch import create_batch
    
    def __init__(self, conf, mask):
        self.config = conf
        self.mask = mask

        self.epoch = 1
        self.training_loss = []
        self.validation_loss = []