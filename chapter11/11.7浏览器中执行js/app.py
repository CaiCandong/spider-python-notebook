from playwright.sync_api import sync_playwright
import time 
url = "https://spa2.scrape.center"
context = sync_playwright().start()
browser=context.chromium.launch(headless=False)
page = browser.new_page()
# 拦截了对'/js/chunk-10192a00.243cb8b7.js'的请求
# 收到的是./chunk.js
# 实现了代码注入
page.route(
    '/js/chunk-10192a00.243cb8b7.js',
    lambda route: route.fulfill(path="./chunk.js")
)
page.goto(url)

def get_token(offset):
    result = page.evaluate('''
    ()=>{return window.encrypt("%s","%s")}
    '''%('/api/movie',offset))
    return result

print(get_token(10))