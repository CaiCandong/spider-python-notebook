import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()


    # Open new page
    page = await context.new_page()

    # Go to https://login2.scrape.center/login
    await page.goto("https://login2.scrape.center/login")

    await page.locator("input[name=\"username\"]").fill("admin")

    # Fill input[name="password"]
    await page.locator("input[name=\"password\"]").fill("admin")

    await page.locator("input:has-text(\"登录\")").click()

    # Go to https://login2.scrape.center/

    await page.goto("https://login2.scrape.center")
    cookies = await context.cookies()
    print(cookies)

    # Close page
    await page.close()

    # ---------------------
    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())