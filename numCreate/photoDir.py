import os
import shutil

# 源文件夹列表（包含要合并的多个文件夹）
source_folders = ["/mnt/ZMJ/SynthText-python3/numCreate/allcategory/电子秤/全部图片",
                  "/mnt/ZMJ/SynthText-python3/numCreate/allcategory/烘箱",
                  "/mnt/ZMJ/SynthText-python3/numCreate/allcategory/冷凝",
                  "/mnt/ZMJ/SynthText-python3/numCreate/allcategory/排风控制",
                  "/mnt/ZMJ/SynthText-python3/numCreate/allcategory/其他",
                  "/mnt/ZMJ/SynthText-python3/numCreate/allcategory/消解仪、水浴锅"]

# 目标文件夹（合并后的图片将保存在这个文件夹）
target_folder = "/mnt/ZMJ/SynthText-python3/numCreate/allphoto"

# 创建目标文件夹
os.makedirs(target_folder, exist_ok=True)

# 初始化文件计数器
file_counter = 0

# 遍历源文件夹列表
for source_folder in source_folders:
    # 获取源文件夹中的所有文件
    files = os.listdir(source_folder)

    # 遍历源文件夹中的文件
    for file in files:
        # 构造源文件的完整路径
        source_path = os.path.join(source_folder, file)

        # 构造目标文件的完整路径，并使用三位数字进行命名（例如：000、001、002）
        target_filename = f"{file_counter:03d}.jpg"
        target_path = os.path.join(target_folder, target_filename)

        # 复制文件到目标文件夹并重命名
        shutil.copyfile(source_path, target_path)

        # 增加文件计数器
        file_counter += 1

print(f"合并完成，共合并了{file_counter}张图片到目标文件夹：{target_folder}")
