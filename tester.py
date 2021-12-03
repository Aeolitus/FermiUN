# %%
from FermiUN import FermiUN
f = FermiUN.from_configfile("./ConfigFiles/testconfig.yaml")
print(f.config)
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