from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup

# ---- Optional - add options to keep the webpage open ----
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome()

driver.set_page_load_timeout(60)
driver.implicitly_wait(60)


def get_bs4_element(url):
    try:
        driver.get(url)
        html = driver.page_source
        return BeautifulSoup(html, 'lxml')
    except WebDriverException as e:
        print("Selenium encountered an exception:", str(e))


stock_overflow = "https://selenium-python.readthedocs.io/api.html"
github = "https://github.com/mosesmccabe"
linkedin = "https://www.linkedin.com/in/moses-mccabe/"

urls = [github, linkedin, stock_overflow]  # List of URLs to scrape

pages_source = []
for url in urls:
    soup = get_bs4_element(url)
    pages_source.append(soup)

print(pages_source)