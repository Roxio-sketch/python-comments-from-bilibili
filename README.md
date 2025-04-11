# python-comments-from-bilibili
# 评论爬取脚本
这是一个基于 Python 和 Selenium 的爬虫脚本，用于从指定网页（例如：Aicu）爬取多页评论，并将评论内容保存到文本文件中。

## 需求
- Python 3.x
- Selenium
- BeautifulSoup（如果使用 HTML 解析）
- Chrome 浏览器及 ChromeDriver

## 安装依赖

1. 安装 Python 依赖包：
   ```bash
   pip install selenium beautifulsoup4
   ```

2. 下载并安装 Chrome 浏览器对应的 `chromedriver`，并确保它与当前的浏览器版本兼容。[ChromeDriver 下载链接](https://sites.google.com/a/chromium.org/chromedriver/)

## 使用方法

1. 将以下代码保存为 `comments.py` 文件：


2. 运行脚本：
   ```bash
   python scrape_comments.py
   ```

   该脚本会自动爬取指定网站的八页评论，并将评论内容保存到 `comments.txt` 文件中。

## 注意事项

- 该脚本当前支持爬取 Aicu 网站的评论，若网站结构发生变化，可能需要调整 `BeautifulSoup` 中的 CSS 选择器。
- 确保 `chromedriver` 与你本地的 Chrome 浏览器版本兼容。
- 若遇到 `SSL handshake` 错误或其他网络问题，通常是与网络连接或浏览器配置有关，不影响爬取过程。

## License

本项目遵循 [MIT 许可证](https://opensource.org/licenses/MIT)。
```
