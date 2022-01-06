from FermiUN import FermiUN
import os
import time
import shutil

starttime = time.time()

#folders = [r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Remeasure', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Heating', \
#    r'Y:\Archiv\2D\Experiment\2021\20210127\Images20210127\Thermo_Unitarity', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_106_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_107_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_108_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_109_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_99_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_99_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th_Const', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th_Const_1', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_103_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_104_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_105_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_106_Th', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Scan_102', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Scan_103', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Scan_104_NoClockthief', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Scan_104_Re', \
#    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Scan_105', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Scan_106', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Scan_107', \
#    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Scan_108', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Scan_Further_9596', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Scan_Further_9798', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Scan_Re_99100', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Scan_Re_109110', \
#    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Scan_Re_Uni']

#folders = [el.replace("\\", "/").replace("Y:", "/afs/physnet.uni-hamburg.de/groups/group-las_m") for el in folders]

f = FermiUN("./ConfigFiles/clusterconfig.yaml")

#if os.path.isdir(f.config.imagefolder):
#    shutil.rmtree(f.config.imagefolder)
#os.makedirs(f.config.imagefolder, exist_ok=True)

#f.import_images(folders, "BrightM")

f.initialize_for_training()
f.train()

endtime = time.time()

print(f"--- Total execution time: {endtime - starttime} seconds ---")