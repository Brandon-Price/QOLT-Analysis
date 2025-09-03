from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time

options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

driver.get("https://codesubmit.io/blog/software-engineer-salary-by-country/")
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

salary_pattern = re.compile(r"\$\s?[\d,]+")
results = []

for img in soup.find_all("img", title=True):
    country = img["title"].strip()
    salary_tag = img.find_next(string=salary_pattern)
    if salary_tag:
        salary = salary_pattern.search(salary_tag).group()
        results.append((country, salary))

driver.quit()