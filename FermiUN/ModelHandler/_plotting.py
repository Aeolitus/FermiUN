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

def plot_inferrence(self, masked : np.array, inferred : np.array, truth : np.array):
    '''
    Plots the result of an inferrence on a single image.
    :param masked: Masked input to the model
    :param inferred: Model output
    :param truth: Ground truth
    '''
    fig = plt.figure(2)
    plt.clf()
    fig.set_facecolor('white')

    plt.subplot(1,4,1)
    plt.imshow(masked, vmin=0.0, vmax=0.9)
    plt.title("Masked Input")

    plt.subplot(1,4,2)
    plt.imshow(truth, vmin=0.0, vmax=0.9)
    plt.title("Target")

    plt.subplot(1,4,3)
    plt.imshow(inferred, vmin=0.0, vmax=0.9)
    plt.title("Model Result")

    plt.subplot(1,4,4)
    plt.imshow(truth-inferred, vmin=0.0, vmax=0.9)
    plt.title("Difference")