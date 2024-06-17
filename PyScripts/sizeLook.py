from PIL import Image

def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        return f"无法获取尺寸: {e}"

# 用法示例
image_path = "../my_photos/01.jpg"
size = get_image_size(image_path)
if isinstance(size, tuple):
    print(f"图片尺寸为：宽度 {size[0]} 像素，高度 {size[1]} 像素")
else:
    print(size)
