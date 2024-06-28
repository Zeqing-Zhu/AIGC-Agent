from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
import os

# 获取当前脚本文件的绝对路径
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, '../data')  # 假设数据目录在src目录的上一层

# 指定tesseract的完整路径
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

def crop_and_preprocess(image_path, crop_box, output_path):
    # 打开原始图像
    img = Image.open(image_path)

    # 裁剪图像
    cropped_img = img.crop(crop_box)

    # 增加对比度
    enhancer = ImageEnhance.Contrast(cropped_img)
    enhanced_img = enhancer.enhance(2.0)

    # 应用锐化
    sharp_img = enhanced_img.filter(ImageFilter.SHARPEN)

    # 保存处理后的图像以便检查
    sharp_img.save(output_path)

    return sharp_img


def extract_text_by_line(img):
    # 使用Tesseract执行OCR，配置参数优化按行识别
    text = pytesseract.image_to_string(img, lang='chi_sim', config='--psm 6')

    # 输出按行分割的文本
    lines = text.split('\n')
    return lines

def save_text(lines, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if line.strip():  # 仅保存非空行
                file.write(line + '\n')

# 定义裁剪区域 (left, upper, right, lower)
crop_box = (2000, 300, 2900, 1350)  # 更新裁剪区域参数

# 图片路径
input_image_path = os.path.join(data_dir, 'toutiao_hotlist.png')
processed_image_path = os.path.join(data_dir, 'processed_toutiao.png')
text_output_path = os.path.join(data_dir, 'extracted_text.txt')

# 处理图像
processed_img = crop_and_preprocess(input_image_path, crop_box, processed_image_path)

# 提取文本
extracted_lines = extract_text_by_line(processed_img)

# 保存文本
save_text(extracted_lines, text_output_path)

print(f"Extracted text saved to {text_output_path}")
