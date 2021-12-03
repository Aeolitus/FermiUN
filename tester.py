# %%
#from FermiUN import FermiUN
#f = FermiUN.from_configfile("./ConfigFiles/testconfig.yaml")
#print(f.config)
# %%
from os import listdir
from os.path import join, isfile, abspath
folderpath = r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Remeasure'
res = img_list = [join(folderpath, el) for el in listdir(folderpath) \
        if 'BrightM' in el and isfile(join(folderpath, el))]
print(res)
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