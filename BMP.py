from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text):
    # 创建一个280x24的白色背景图片
    img_width = 280
    img_height = 24
    image = Image.new("RGBA", (img_width, img_height), (255, 255, 255, 0))  # 透明背景
    
    draw = ImageDraw.Draw(image)

    # 设置字体和大小
    try:
        # 尝试加载系统的 Arial 字体文件
        font_path = "PangMenZhengDaoXiXianTi-2.ttf"  # 替换为你的中文字体文件路径
        font = ImageFont.truetype(font_path, 20)
    except IOError:
        # 如果无法找到，将使用默认字体
        font = ImageFont.load_default()

    # 获取文本的边界框
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # 右下角 x - 左上角 x
    text_height = text_bbox[3] - text_bbox[1]  # 右下角 y - 左上角 y

    # 计算文本位置，使其居中
    text_x = (img_width - text_width) / 2
    text_y = (img_height - text_height) / 2
    # 通过增加基线偏移量来调整垂直位置
    baseline_offset = -3  # 根据字体的特性进行适当调整
    text_y += baseline_offset
    # 绘制紫色描边
    outline_color = (28, 24, 128)  # 紫色
    for offset in [-1, 0, 1]:  # 描边效果
        draw.text((text_x + offset, text_y), text, font=font, fill=outline_color)
        draw.text((text_x, text_y + offset), text, font=font, fill=outline_color)

    # 绘制白色文本
    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

    # 保存为BMP格式
    image.save("output.png")

# 示例调用
create_image_with_text("asdasd")
