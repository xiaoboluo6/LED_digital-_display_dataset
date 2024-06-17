import h5py

# 打开MAT文件
# mat_file = h5py.File('./sevenTest/ucmSeven.mat', 'r')
mat_file = h5py.File('./ucm.mat', 'r')

# 遍历MAT文件中的所有内容，包括数据集的详细信息
def print_contents(name, obj):
    if isinstance(obj, h5py.Group):
        print(f"Group: {name}")
    elif isinstance(obj, h5py.Dataset):
        print(f"Dataset: {name}")
        print(f"Shape: {obj.shape}")
        print(f"Dtype: {obj.dtype}")
        print(f"Value: {obj[:]}")  # 打印部分数据（可根据需要修改）

# 使用visititems方法遍历文件内容
mat_file.visititems(print_contents)

# 关闭MAT文件
mat_file.close()
