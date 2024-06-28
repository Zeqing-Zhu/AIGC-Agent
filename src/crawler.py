from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

# 获取当前脚本所在文件夹的路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '..', 'data')  # 假设数据目录在src目录的上一层

def setup_driver():
    # 设置浏览器驱动选项
    options = Options()
    options.add_argument("--start-maximized")  # 最大化窗口
    options.add_argument('--disable-gpu')  # 禁用GPU加速
    options.add_argument('--no-sandbox')  # 禁用沙盒模式
    options.add_argument('--disable-dev-shm-usage')  # 减少Dev shm使用
    service = Service(ChromeDriverManager().install())  # 自动管理驱动
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scroll_to_element(driver, element):
    # 将网页滚动到指定元素的位置
    desired_y = (element.size['height'] / 2) + element.location['y']
    current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script(
        'return window.pageYOffset')
    scroll_y_by = desired_y - current_y
    driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

def fetch_toutiao_hotlist(driver):
    # 访问今日头条热榜页面并截图
    driver.get('https://www.toutiao.com/ch/news_hot/')

    try:
        # 等待热榜元素加载完成
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.home-hotboard'))
        )
        scroll_to_element(driver, element)  # 滚动到该元素
        print("Element found and scrolled to successfully.")
    except TimeoutException:
        # 如果在指定时间内没有找到元素，则打印错误消息
        print("Failed to find the specified element within the given time. Check the CSS selector or network conditions.")
        return

    time.sleep(2)  # 等待页面加载完成

    screenshot_path = os.path.join(DATA_DIR, 'toutiao_hotlist.png')
    driver.save_screenshot(screenshot_path)  # 保存截图
    print(f"Screenshot saved to {screenshot_path}")

def main():
    driver = setup_driver()
    try:
        fetch_toutiao_hotlist(driver)
    finally:
        driver.quit()  # 确保无论如何都会关闭浏览器

if __name__ == '__main__':
    main()
