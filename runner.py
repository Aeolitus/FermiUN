from FermiUN import FermiUN

folders = [r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Remeasure', \
    r'Y:\Archiv\2D\Experiment\2021\20210202\Images20210202\Thermo_Heating', \
    r'Y:\Archiv\2D\Experiment\2021\20210127\Images20210127\Thermo_Unitarity', \
    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_106_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_107_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_108_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210124\Images20210124\Cal_109_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_99_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_99_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th_Const', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_102_Th_Const_1', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_103_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_104_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_105_Th', \
    r'Y:\Archiv\2D\Experiment\2021\20210120\Images20210120\Cal_106_Th']

# TODO: Fix the placeholders in the config file, make a real one.
f = FermiUN("./ConfigFiles/testconfig.yaml")
#f.import_images(folders, "BrightM")

#f.initialize_for_training()
#f.train()