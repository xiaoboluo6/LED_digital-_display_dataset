import os
import h5py
import cv2

# 定义文件路径和文件夹名称
file_name = './sevenResult.h5'
output_folder = '1wResult_jpg_txt'

# 创建输出文件夹
os.makedirs(output_folder, exist_ok=True)

# 打开HDF5文件
db = h5py.File(file_name, 'r')

# 获取数据集列表
dsets = sorted(db['data'].keys())

# 遍历每个数据集
for k in dsets:
    # 从HDF5中获取RGB图像
    rgb = db['data'][k][...]

    # 从HDF5中获取WordBB内容
    wordBB = db['data'][k].attrs['wordBB']

    # 从HDF5中获取文字信息
    txt = db['data'][k].attrs['txt']

    # 保存RGB图像到文件夹
    img_filename = os.path.join(output_folder, f'{k}.jpg')
    cv2.imwrite(img_filename, cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))

    # 保存WordBB内容和文字信息到文本文件
    txt_filename = os.path.join(output_folder, f'{k}.txt')
    with open(txt_filename, 'w') as txt_file:
        for i in range(wordBB.shape[-1]):
            bb = wordBB[:, :, i]
            for j in range(4):
                txt_file.write(f'{bb[0, j]:.2f},{bb[1, j]:.2f} ')
            txt_file.write(f'{txt[i]}\n')

# 关闭HDF5文件
db.close()

print("保存完成。")
