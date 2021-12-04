import numpy as np
import tqdm as tqdm
import gc
from os.path import join
from os import remove

def train_model(self):
    '''
    Trains the model and saves the current state to the folder. 
    '''

    trainBatches = len(self.config.trainlist) // self.config.batch_size
    valBatches = len(self.config.validationlist) // self.config.batch_size

    while self.epoch <= self.config.max_epochs:
        shuffled_trainlist = np.arange(len(self.config.trainlist))
        shuffled_validationlist = np.arange(len(self.config.validationlist))
        np.random.shuffle(shuffled_trainlist)
        np.random.shuffle(shuffled_validationlist)

        current_training_loss = 0
        current_validation_loss = 0

        for i in tqdm(range(trainBatches)):
            X, Y = self.create_batch(self.config.trainlist, shuffled_trainlist \
                [i * self.config.batch_size : (i + 1) * self.config.batch_size])
            current_training_loss = current_training_loss \
                + self.model.train_on_batch(x=X, y=Y) / trainBatches
        print(f"Epoch {self.epoch} training loss: {current_training_loss}")

        for i in tqdm(range(valBatches)):
            X, Y = self.create_batch(self.config.validationlist, shuffled_validationlist \
                [i * self.config.batch_size : (i + 1) * self.config.batch_size])
            current_validation_loss = current_validation_loss \
                + self.model.test_on_batch(x=X, y=Y) / valBatches
        print(f"Epoch {self.epoch} validation loss: {current_validation_loss}")

        self.training_loss = np.append(self.training_loss, current_training_loss)
        self.validation_loss = np.append(self.validation_loss, current_validation_loss)

        # TODO: Plot the loss curve

        # Save the current state of the model 
        self.model.save(join(self.config.imagefolder, "model_e" + str(self.epoch) + ".h5"))
        np.save(join(self.config.imagefolder, 'model_training_loss.npy'), self.training_loss)
        np.save(join(self.config.imagefolder, 'model_validation_loss.npy'), self.validation_loss)
        
        gc.collect() # Is this neccessary?

        self.epoch = self.epoch + 1