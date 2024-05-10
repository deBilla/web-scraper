import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://medium.com/@billa-code'

driver = webdriver.Chrome()
driver.get(url)

time.sleep(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')
titles = soup.find_all('div', class_ = 'title')
bodies = soup.find_all('div', class_='i_info')

for title, body in zip(titles, bodies):
    print("Title:", title.text.strip())
    print("Body:", body.text.strip())
    print()
