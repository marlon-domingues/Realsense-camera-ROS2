import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/WVU-AD/md00126/real_sense_camera/install/RGBD_data'
