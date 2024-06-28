# README：自动化今日头条新闻生成Agent


## 项目简介
本项目自动从头条热榜截取屏幕图片，并从中提取文本内容，适用于新闻热点分析和数据采集。项目利用 Python、Selenium 和 Tesseract OCR 实现自动化截图和文本提取。

## 系统需求
- Python 3.8+
- Selenium
- Pillow
- pytesseract
- Tesseract-OCR

## 安装指南

### Python 依赖安装
安装必要的 Python 库:
```bash
pip install selenium pytesseract pillow webdriver-manager
```

### Tesseract-OCR 安装
Tesseract 是一个开源的 OCR 引擎，用于从图片中识别文本。

- **Windows:**
  下载并安装 Tesseract 从 [GitHub Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki)。安装时选择包含中文简体的语言包。

- **macOS:**
  使用 Homebrew 安装 Tesseract 及中文简体语言包:
  ```bash
  brew install tesseract
  brew install tesseract-lang
  ```

- **Linux:**
  使用 apt-get 安装 Tesseract 及中文简体语言包:
  ```bash
  sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim
  ```

### 环境变量设置
确保 Tesseract 的安装路径已添加到您的系统环境变量中。对于中文文本识别，确保 `chi_sim.traineddata` 文件已安装。

## 运行说明

### 运行 crawler.py
该脚本使用 Selenium 自动打开 Chrome 浏览器，访问今日头条热榜并截图保存。
```bash
python3 crawler.py
```

### 运行 text_extraction.py
该脚本处理 `crawler.py` 保存的截图，使用 pytesseract 进行图像预处理并提取文本。
```bash
python3 text_extraction.py
```

## 文件说明
- `crawler.py` —— 自动浏览网页并截图的脚本。
- `text_extraction.py` —— 图像处理和文本提取脚本。

## 许可
本项目采用 [MIT 许可证](LICENSE)。

---

这个 README 提供了一个清晰的指导，说明了如何设置和运行您的项目，以及如何处理潜在的安装和配置问题。您可以根据项目的实际需求进一步调整或扩展这个文档。