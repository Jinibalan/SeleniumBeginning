import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="driver/chromedriver-3")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element(By.ID, "fromCity").click()
driver.find_element(By.CSS_SELECTOR, "input[placeholder='From']").send_keys("del")

cities = driver.find_elements(By.CSS_SELECTOR, "p[class*='blackText']")
print(len(cities))
for city in cities:
    if city.text == "Del Rio,United States":
        city.click()
        break
time.sleep(4)
driver.find_element(By.XPATH, "//p[text()='Delhi, India']").click()
driver.close()