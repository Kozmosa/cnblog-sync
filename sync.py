import json
import os
import logging
import encode
import preprocess
from selenium import webdriver

# tool functions
get_pre_text = lambda browser: browser.find_element_by_css_selector("pre").text
preprocessor = preprocess.PreProcessor()

# logger init
fhandler = logging.FileHandler("log/blogsync.log", mode='w', delay=False)
flogger = logging.getLogger("blogsync")
flogger.addHandler(fhandler)
flogger.setLevel(logging.INFO)


def login_automaticlly(browser, username, password):
    browser.get(
        "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fi-beta.cnblogs.com%2Fposts")
    wname = browser.find_element_by_css_selector("#LoginName")
    wpass = browser.find_element_by_css_selector("#Password")
    wname.send_keys(username)
    wpass.send_keys(password)
    blogin = browser.find_element_by_css_selector("#submitBtn")
    blogin.click()
    input("請在完成機器驗證碼之後按下回車")


def login(browser):
    browser.get(
        "https://account.cnblogs.com/signin?returnUrl=https%3A%2F%2Fi-beta.cnblogs.com%2Fposts")
    input("請在完成登錄之後按下回車")

def get_list(browser):
    browser.get("https://i-beta.cnblogs.com/api/posts/list")
    total = json.loads(browser.find_element_by_css_selector("pre").text)['postsCount']
    total_page = math.ceil(total/10)
    
    # debug
    flogger.info("總共有 %s 頁數據" % str(total_page))

    post_list = []
    for page in range(1, total_page + 1):
        browser.get("https://i-beta.cnblogs.com/api/posts/list?p=%s" % str(page))
        json_wrapper = browser.find_element_by_css_selector("pre")
        data = json.loads(json_wrapper.text)
        postList = data['postList']
        
        # debug
        flogger.info("獲取到了第%s頁的文章列表" % str(page))
        
        post_list+=postList
    post_list.pop()
    return post_list

def download_post_markdown(browser, post_list):
    for post in post_list:
        details = {
            'id': post['id'],
            'title': post['title'],
            'date': post['datePublished'].split("T")[0],
            'author': "xuyang1638"
        }

        id = post['id']
        title = post['title']
        filename = details['title'] + ".md"

        api_url = "https://www.cnblogs.com/kozumi/p/%s.md" % id
        flogger.info("正在下載文章，標題爲“%s”" % title)
        
        browser.get(api_url)
        # yaml_data = get_meta_data(title, author, time)
        content = browser.find_element_by_css_selector("pre").text
        content = preprocessor.process(content, details)
        save_post(filename, content)

def save_post(filename, content):
    with open("posts/" + filename, 'w') as f:
        f.write(content)

def get_meta_data(title, author, date):
    template = """---
title: TITLE
author: AUTHOR
date: DATE
mathjax: true
---
"""

    result = template.replace("TITLE", title)
    result = result.replace("AUTHOR", author)
    result = result.replace("DATE", date)
    return result

def firstrun():
    if !os.path.exists("posts"):
        os.mkdir("posts")
    if !os.path.exists("log"):
        os.mkdir("log")

def main():
    # judgement of first run
    firstrun()

    browser = webdriver.Chrome()

    flogger.info("登錄管理後臺")
    login(browser)

    flogger.info("獲取文章列表")
    post_list = get_list(browser)

    flogger.info("開始下載文章")

    try:
        download_post_markdown(browser, post_list)
    except:
        flogger.error("Download Articles Error")
    
    # optimize article files
    # fix encoding problems
    flogger.info("優化文章檔案")
    flogger.info("修復編碼問題")
    files = encode.get_files('./posts/')
    for file in files:
        flogger.info("正在修復檔案 '%s' 的編碼問題" % file)
        content = encode.encode(file)
        encode.write(file, content)

    # move files into hexo folder
    # 日後再寫,目前只用手動搬運就好了:)

    flogger.info("修復完畢,存儲爲utf-8編碼格式")
    flogger.info("全部工作已完成, 謝謝使用")
    
    if input("請選擇是否要退出瀏覽器（y/n）：") == "n":
        pass
    else:
        browser.close()


if __name__ == "__main__":
    main()
