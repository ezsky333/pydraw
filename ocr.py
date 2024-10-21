from paddleocr import PaddleOCR
from PIL import Image

def recognize_text_in_image(image_path):
    """
    识别图片中的文本，并返回识别结果和图片的像素大小。
    
    :param image_path: 图片的文件路径
    :return: 识别的字符串和图片的像素大小 (width, height)
    """
    ocr = PaddleOCR(use_angle_cls=True, lang='en')  # lang 参数可以设置为 'ch'、'en' 等
    
    # 打开图片以获取其尺寸
    with Image.open(image_path) as img:
        width, height = img.size

    result = ocr.ocr(image_path, cls=True)

    recognized_text = ''
    for line in result:
        for word_info in line:
            recognized_text += word_info[1][0] + ' '

    return recognized_text.strip(), (width, height)

# 示例用法
# Example usage
text, dimensions = recognize_text_in_image('output.png')
print("Recognized Text:", text)
print("Image Dimensions:", dimensions)