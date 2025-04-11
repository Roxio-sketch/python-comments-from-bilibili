from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

# 修改为实际的 chromedriver 路径
service = Service(executable_path=r'D:\chromedriver-win64\chromedriver.exe')
service.start()

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 如果你不需要打开浏览器界面

driver = webdriver.Chrome(service=service, options=options)

# 设置目标 URL 和总页数
base_url = 'https://www.aicu.cc/reply.html?uid=212535360&pn='
total_pages = 8  # 总页数

# 遍历所有页面
for page_num in range(1, total_pages + 1):
    url = base_url + str(page_num)
    print(f"正在处理第 {page_num} 页，访问 URL: {url}")

    # 打开目标网页
    driver.get(url)

    # 使用显式等待来确保页面加载完成
    try:
        # 等待页面中某个元素加载完成，例如评论容器
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'message'))  # 替换为实际评论的 class 名
        )
    except Exception as e:
        print(f"加载失败：{e}")
        continue  # 如果加载失败，跳过这一页

    # 获取页面源代码
    html_content = driver.page_source

    # 使用 BeautifulSoup 解析网页
    soup = BeautifulSoup(html_content, 'html.parser')

    # 假设评论在 class 为 'message' 的 div 中
    comments = soup.find_all('div', class_='message')

    # 保存评论到文本文件
    with open('comments.txt', 'a', encoding='utf-8') as file:  # 使用 'a' 追加模式
        for comment in comments:
            file.write(comment.get_text(strip=True) + '\n')

    print(f"第 {page_num} 页评论已保存。")

    # 等待一段时间，防止请求过快
    time.sleep(2)

# 关闭浏览器
driver.quit()

print("所有评论已保存到 comments.txt")
