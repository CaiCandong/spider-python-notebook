from playwright.sync_api import Playwright, sync_playwright, expect

js="""
Object.defineProperties(navigator, {webdriver:{get:()=>undefined}});
"""
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()
    page.add_init_script(js)

    # Go to http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml?version=tem
    page.goto("http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml?version=tem")

    # Open new page
    page1 = context.new_page()

    # Go to http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml?version=tem
    page1.goto("http://pss-system.cnipa.gov.cn/sipopublicsearch/portal/uilogin-forwardLogin.shtml?version=tem")

    # Go to http://pss-system.cnipa.gov.cn/
    page1.goto("http://pss-system.cnipa.gov.cn/")
    
    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
