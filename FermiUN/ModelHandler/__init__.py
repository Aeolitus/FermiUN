__all__ = ["_define_model", "_init_model", "_train_model"]

class ModelHandler(object): 
    # Import Methods from Files
    from ._define_model import define_model
    from ._init_model import init_model
    from ._train_model import train_model
    
    def __init__(self, conf):
        self.config = conf