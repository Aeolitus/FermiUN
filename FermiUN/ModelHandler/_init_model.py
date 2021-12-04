from tensorflow.keras import backend
from tensorflow.keras.optimizers import Adam

def init_model(self):
    '''
    Set up the model from scratch.
    '''
    backend.clear_session()
    self.model = self.define_model()
    self.model.summary()
    opt = Adam(lr=self.config.learning_rate)
    self.model.compile(optimizer=opt, loss='mse')