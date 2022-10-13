#   в CMD нужно установить Селениум: C:\Users\lavrushko\Desktop\Учеба\Parsing\venv\Scripts\pip install selenium
#  Скачать и запустить Chromedriver (для хрома)
# Установить так же pymongo для поднятия базы данных -  pip install pymongo
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

db = []

chrome_options = Options()
chrome_options.add_argument("disable-notifications")
chrome_options.add_argument("--windows-size=1920,1080")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options)
driver.implicitly_wait(5)

url = 'https://www.mvideo.ru'
driver.get(url)
time.sleep(2)

driver.execute_script("window.scrollTo(0, window.scrollY + 1400)")
time.sleep(2)

#driver.page_source
button_trend = driver.find_element(By.XPATH,"//button[@CLASS='tab-button ng-star-inserted']")
button_trend.click()

#trends = driver.find_element(By.XPATH, "//mvid-carousel[@class='carusel ng-star-inserted']")
trends = driver.find_element(By.XPATH, "//*[contains(@style,'grid-template-columns: repeat(16, 20rem')]")

goods = trends.find_elements(By.XPATH, "//div[contains(@class,'ng-star-inserted')]")

names = goods[0].find_elements(By.XPATH, "//div[@class='title']")
links = goods[0].find_elements(By.XPATH, "//div[@class='title']/a[@href]")
prices = goods[0].find_elements(By.XPATH, "//span[@class='price__main-value']")

for i in range(len(names)-3):
    item = {}
    item['name'] = names[i+3].text
    item['link'] = links[i+3].get_attribute("href")
    item['price'] = prices[i+3].text

    db.append(item)

driver.quit()

for item in db:
    print(item)
