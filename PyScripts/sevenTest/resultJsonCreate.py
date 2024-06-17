from PIL import Image
import os

# yolo的class : label
classToLabel = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': '-', '11':'word'}

# label : yolo的class
labelToClass = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '-': '10', 'word':'11'}





def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error reading image size: {e}")
        return None

def xywh_from_corners(corners, image_width,image_height):
    x_min = min(corners[0][0], corners[1][0], corners[2][0], corners[3][0])
    y_min = min(corners[0][1], corners[1][1], corners[2][1], corners[3][1])
    x_max = max(corners[0][0], corners[1][0], corners[2][0], corners[3][0])
    y_max = max(corners[0][1], corners[1][1], corners[2][1], corners[3][1])

    width = x_max - x_min
    height = y_max - y_min
    x_center = (x_min + x_max) / (2 * image_width)
    y_center = (y_min + y_max) / (2 * image_height)

    return x_center, y_center, width / image_width, height / image_height


def get_jpg_filenames(directory):
    jpg_filenames = []
    for filename in os.listdir(directory):
        if filename.lower().endswith(".jpg"):
            # 提取文件名中的前缀（假设文件名是 "00.jpg"）
            prefix = filename.split(".")[0]
            jpg_filenames.append(prefix)
    return jpg_filenames


if __name__ == '__main__':
    directory = "./SevenResult_jpg_txt"
    jpg_filenames = get_jpg_filenames(directory)
    current_directory = os.getcwd()
    full_path = os.path.join(current_directory, "SevenResult_jpg_txt")
    print("Full Path:", full_path)


    # shuchu lujing
    output_folder = os.path.join(current_directory, "Yolo_label")
    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)


    for each in jpg_filenames:
        image_path = os.path.join(full_path,each+".jpg")
        charTxt_path = os.path.join(full_path,each+"char.txt")
        wordTxt_path = os.path.join(full_path,each+"word.txt")



        yolo_label_txt = os.path.join(output_folder, f'{each}.txt')
        with open(yolo_label_txt, 'w') as yolo_label_file:
            try:
                image_width,image_height = get_image_size(image_path)

                # 先处理每个字符
                with open(charTxt_path, 'r') as file:
                    for line in file:
                        # 对每一行的内容进行处理
                        data = line
                        coords_and_class = data.split()
                        corners = [list(map(float, point.split(','))) for point in coords_and_class[:-1]]
                        label = coords_and_class[-1]

                        yolo_class = labelToClass[label]
                        x_center, y_center,width_per,height_per = xywh_from_corners(corners,image_width,image_height)

                        yolo_line = " ".join([yolo_class, str(x_center), str(y_center), str(width_per), str(height_per)])
                        yolo_label_file.write(f'{yolo_line}\n')

                # 再处理整体的单词
                with open(wordTxt_path, 'r') as file:
                    for line in file:
                        # 对每一行的内容进行处理
                        data = line
                        coords_and_class = data.split()
                        corners = [list(map(float, point.split(','))) for point in coords_and_class[:-1]]
                        label = coords_and_class[-1]

                        yolo_class = "11"
                        x_center, y_center,width_per,height_per = xywh_from_corners(corners,image_width,image_height)

                        yolo_line = " ".join([yolo_class, str(x_center), str(y_center), str(width_per), str(height_per)])
                        yolo_label_file.write(f'{yolo_line}\n')


            except Exception as e:
                print(f"Error reading file: {e}")

