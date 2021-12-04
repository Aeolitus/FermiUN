import numpy as np
import matplotlib.pyplot as plt

def plot_loss_curve(self):
    '''
    Plots the continuous loss for the training loop
    '''
    
    fig = plt.figure(1)
    plt.clf()
    fig.set_facecolor('white')

    if self.epoch < 50:
        plt.semilogy(self.training_loss, label='training')
        plt.semilogy(self.validation_loss, label='validation')
    else:
        plt.loglog(self.training_loss, label='training')
        plt.loglog(self.validation_loss, label='validation')
    plt.legend()

    plt.show(block=False)
    plt.pause(0.001)