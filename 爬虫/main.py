import requests
from bs4 import BeautifulSoup


#  错误示范
def get_web_content(url):
    try:
        # 发送GET请求获取网页内容
        response = requests.get(url)
        # 检查请求是否成功
        if response.status_code == 200:
            # 使用BeautifulSoup解析网页内容
            soup = BeautifulSoup(response.text, 'html.parser')
            # 这里只是简单返回网页标题
            return soup.title.text
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None
    except Exception as e:
        print(f"发生错误：{e}")
        return None


# 示例使用
url = "https://www.baidu.com"
print(get_web_content(url))