__all__ = ["_crop_and_copy_from_folder", "_make_train_validation_test_split", "_create_batch", "_generate_mask"]

class DataHandler(object):
    # Import Methods from Files
    from ._crop_and_copy_from_folder import crop_and_copy_from_folder
    from ._make_train_validation_test_split import make_train_validation_test_split
     
    def __init__(self, conf, mask):
        self.config = conf
        self.mask = mask