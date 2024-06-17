import h5py

# 打开 HDF5 文件
file_name = '../data/dset.h5'
#file_name = 'seg_uint16.h5'
with h5py.File(file_name, 'r') as dbo:
    # 递归函数，用于遍历 HDF5 文件中的组和数据集
    def print_hdf5_items(name, obj):
        if isinstance(obj, h5py.Group):
            print("Group:", name)
            for key, item in obj.items():
                print_hdf5_items(key, item)
        elif isinstance(obj, h5py.Dataset):
            print("Dataset:", name)
            # 打印数据集的内容（前几个元素）
            data = obj[:]
            print(data.shape)
            # if data.shape[0] > 5:  # 如果数据集很大，只打印前5个元素
            #     print(data[:5])
            # else:
            #     print(data)

    # 遍历 HDF5 文件的根（Root）
    dbo.visititems(print_hdf5_items)

# import h5py
#
# # 打开 HDF5 文件
# file_name = 'seg_uint16.h5'
#
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
#
#             # 检查是否有 'area' 和 'label' 属性
#             if 'area' in obj.attrs and 'label' in obj.attrs:
#                 area = obj.attrs['area']
#                 label = obj.attrs['label']
#                 print("area:", area)
#                 print("label:", label)
#
#     # 遍历 HDF5 文件的根（Root）
#     dbo.visititems(print_hdf5_items)
