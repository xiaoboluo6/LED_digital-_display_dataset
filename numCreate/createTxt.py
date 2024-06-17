# import random
#
# # 设置文件名和行数
# file_name = '../data/newsgroup/nums.txt'
# num_lines = 500000
#
# # 生成文件
# with open(file_name, 'w') as file:
#     for i in range(num_lines):
#         # 随机选择数字类型（正整数或小数）
#         num_type = random.randint(0, 9)
#
#         # 随机生成数字，有一半的概率为整数，另一半的概率为小数
#         if 0 <= num_type <= 8:
#             num_decimal_places = random.randint(1, 3)  # 随机确定小数点位数（1至3位）
#             number = round(random.uniform(0, 1000), num_decimal_places)
#         else:
#             # 随机确定数字的位数
#             num_digits = random.choice([1, 2, 3, 4]) if random.random() < 0.3 else random.randint(3, 4)
#             number = random.randint(0, 10 ** num_digits - 1)
#
#         # 随机选择是否添加正负号，确保每 15 行中有一个数带上正负号
#         if i % 10 == 0:
#             number = random.choice(['-']) + str(number)
#
#         # 将数字添加到当前行
#         line = str(number) + '\n'
#
#         # 写入文件
#         file.write(line)
#
# print(f'{num_lines}行文本已生成到文件：{file_name}')
import random

# 设置文件名和行数
file_name = '../data/newsgroup/allone.txt'
num_lines = 500000

# 生成文件
with open(file_name, 'w') as file:
    for i in range(num_lines):

        # 随机确定数字的位数
        number = 1816

        # 随机选择是否添加正负号，确保每 15 行中有一个数带上正负号
        if i % 10 == 0:
            number = random.choice(['-']) + str(number)

        # 将数字添加到当前行
        line = str(number) + '\n'

        # 写入文件
        file.write(line)

print(f'{num_lines}行文本已生成到文件：{file_name}')