# -*- coding: utf-8 -*-
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome 浏览器位置
chrome_exe =  r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# chrome 浏览器驱动位置
chrome_driver = r'C:\Users\root\anaconda3\Scripts\chromedriver.exe'

# 驱动参数配置
options = Options()
# option.add_argument('headless')  # 后台运行

option = webdriver.ChromeOptions()
options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(
    chrome_options=options,
    options=options, 
    executable_path=chrome_driver)
driver.get('https://resources.marine.copernicus.eu/product-detail/GLOBAL_MULTIYEAR_PHY_001_030/DATA-ACCESS')
# driver.quit()

# def get_patents_list(word, App_or_key=True, page=1):
#     '''google 专利下载专利文件及 生成专利清单，默认申请人'''
#     keys = f"assignee={word}" if App_or_key else f"q={word}"  # inventor=任
#     main_url = r'https://patents.google.com/?{0}&language=CHINESE&num=100&page={1}'.format(keys, page)
#     option = webdriver.ChromeOptions()
#     # option.add_argument('headless')  # 后台运行
#     option.add_experimental_option('excludeSwitches', ['enable-automation'])
#     driver = webdriver.Chrome(options=option)
#     # driver.maximize_window()  # 最大化
#     # driver.set_window_size(1200, 800) # 大小
#     driver.implicitly_wait(1)
#     driver.get(main_url)
#     # print(main_url)

#     # 开始注释
#     # pdf 下载接口
#     pdfs = [i.get_attribute("href") for i in
#             driver.find_elements_by_css_selector('a.pdfLink.style-scope.search-result-item')]
#     # print("pdfs:", pdfs)
#     names = [i.text + ".pdf" for i in driver.find_elements_by_css_selector('h3 span#htmlContent.style-scope.raw-html')]
#     names = [x.replace("/", "") for x in names]
#     # print("names:", names)
#     #
#     nums = [i.text for i in driver.find_elements_by_css_selector('span.style-scope.search-result-item') if
#             "CN" in i.text]
#     # nums = [i.text for i in driver.find_elements_by_css_selector('span.style-scope.search-result-item')]
#     nums = [x for x in list(set(nums)) if len(x) != 2]
#     # print("nums:", nums)
