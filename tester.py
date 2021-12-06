# %%
#from FermiUN import FermiUN
#f = FermiUN.from_configfile("./ConfigFiles/testconfig.yaml")
#print(f.config)
# %%
d1 = 64
d2 = 128
d3 = 256
d4 = 512
d5 = 1024
b_momentum=0.99

minS = 20 # smallest size of layer at the bottom of the U
inS = minS
for i in range(4):
    inS = (inS+4)*2
inS = inS+4

upS = [inS-4]
for i in range(3):
    s = int(upS[-1]/2-4)
    upS = np.append(upS,s)

downS = minS
downS = [int(downS*2)]
for i in range(3):
    s = int(downS[-1]-4)*2
    downS = np.append(downS,s)
downS = np.flip(downS)
lastS = downS[0]-6
crop = (upS-downS)/2

cropL = int((lastS-12*2) / 2)
cropL1 = int(crop[0])
cropL2 = int(crop[1])
cropL3 = int(crop[2])
cropL4 = int(crop[3])
# %%
from FermiUN import FermiUN
FermiUN.create_config_file("./ConfigFiles/testconfig.yaml")
# %%
from FermiUN import FermiUN
f = FermiUN("./ConfigFiles/testconfig.yaml")
print(f.modelhandler.config)
# %%
from FermiUN import FermiUN
from os import listdir, mkdir
from os.path import join, exists
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

self = FermiUN("./ConfigFiles/testconfig.yaml")
folderpath = r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Remeasure'

# Method header
if not exists(folderpath):
    raise Exception("Source imagefolder does not exist.")

target_folder = self.config.imagefolder
if not exists(target_folder):
    mkdir(target_folder)

top = int(self.config.image.center_y-self.config.image.width/2.0)
left = int(self.config.image.center_x-self.config.image.width/2.0)
if top < 0 or left < 0:
    raise Exception("Crop window exceeds image bounds.")

img_list = [join(folderpath, el) for el in listdir(folderpath) if 'BrightM' in el]

img = io.imread(img_list[0])
img = img[top : top + self.config.image.width, \
    left : left + self.config.image.width]

# Rescale and cut of outliers
# TODO: This should probably be automatically determined from the images
img = img / self.config.image.max_value
img[img > 1.0] = 1.0 # TODO: Should this be somehow marked as an outlier?
img[img < 0.0] = 0


img_number = len(listdir(target_folder))
target_name = target_folder + '/' + self.config.imageprefix + str(img_number)

np.save(target_name, img)