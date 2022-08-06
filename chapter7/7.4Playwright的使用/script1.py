from playwright.sync_api import sync_playwright

# 浏览器上下文管理器 p 
with sync_playwright() as p:
    #  Chromium、Firefox 以及 Webkit 浏览器实例
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        # launch 方法返回的是一个 Browser 对象,打开浏览器
        browser = browser_type.launch(headless=False)
        # new_page 方法，相当于新建了一个选项卡
        page = browser.new_page()
        # 调用 goto，就是加载某个页面
        page.goto('https://www.baidu.com')
        # 截图
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        print(page.title())
        browser.close()