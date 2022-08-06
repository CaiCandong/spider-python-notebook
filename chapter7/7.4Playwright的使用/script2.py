import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # 注意：如果不设置为 False，默认是无头模式启动浏览器，我们看不到任何窗口。
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            print(await page.title())
            await browser.close()
asyncio.run(main())