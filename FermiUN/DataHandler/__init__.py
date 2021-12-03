__all__ = ["_crop_and_copy_from_folder", "_make_train_validation_test_split", "_create_batch", "_generate_mask"]

class DataHandler(object):
    # Import Methods from Files
    from ._crop_and_copy_from_folder import crop_and_copy_from_folder
    from ._make_train_validation_test_split import make_train_validation_test_split
    from ._create_batch import create_batch
    from ._generate_mask import generate_mask
     
    def __init__(self, conf):
        self.config = conf