import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="driver/chromedriver-3")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
driver.find_element(By.NAME, "email").send_keys("Shetty")

driver.find_element(By.ID, "exampleCheck1").click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
time.sleep(4)
dropdown.select_by_index(0)

driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(4)
message = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "success" in message
driver.close()