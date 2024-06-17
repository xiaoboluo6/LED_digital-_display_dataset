# import h5py
#
# # 打开 HDF5 文件
# #file_name = '../data/dset.h5'
# #file_name = 'depth.h5'
# file_name = '../results/my_file_result.h5'
# with h5py.File(file_name, 'r') as dbo:
#     # 递归函数，用于遍历 HDF5 文件中的组和数据集
#     def print_hdf5_items(name, obj):
#         if isinstance(obj, h5py.Group):
#             print("Group:", name)
#             for key, item in obj.items():
#                 print_hdf5_items(key, item)
#         elif isinstance(obj, h5py.Dataset):
#             print("Dataset:", name)
#             # 打印数据集的内容（前几个元素）
#             data = obj[:]
#             print(data.shape)
#             # if data.shape[0] > 5:  # 如果数据集很大，只打印前5个元素
#             #     print(data[:5])
#             # else:
#             #     print(data)
#
#     # 遍历 HDF5 文件的根（Root）
#     dbo.visititems(print_hdf5_items)

from __future__ import division
import os
import os.path as osp
import numpy as np
import matplotlib.pyplot as plt
import h5py
from common import *
file_name = '../results/my_file_result.h5'
db = h5py.File(file_name, 'r')
dsets = sorted(db['data'].keys())
print ("total number of images : ", colorize(Color.RED, len(dsets), highlight=True))
for k in dsets:
    rgb = db['data'][k][...]
    charBB = db['data'][k].attrs['charBB']
    wordBB = db['data'][k].attrs['wordBB']
    txt = db['data'][k].attrs['txt']
    print("rgb Shape:", rgb.shape)
    print("charBB Shape:", charBB.shape)
    print("wordBB Shape:", wordBB.shape)
    print("wordBB", wordBB)
    print("txt", txt)