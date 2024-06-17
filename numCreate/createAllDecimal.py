import random

# 设置文件名和行数
file_name = 'allDecimal.txt'
num_lines = 300000

# 生成文件
with open(file_name, 'w') as file:
    for i in range(num_lines):
        # 随机选择数字类型（正整数或小数）

        num_decimal_places = random.randint(1, 3)  # 随机确定小数点位数（1至3位）
        number = round(random.uniform(0, 1000), num_decimal_places)

        # 随机选择是否添加正负号，确保每 15 行中有一个数带上正负号
        if i % 10 == 0:
            number = random.choice(['-']) + str(number)

        # 将数字添加到当前行
        line = str(number) + '\n'

        # 写入文件
        file.write(line)

print(f'{num_lines}行文本已生成到文件：{file_name}')
