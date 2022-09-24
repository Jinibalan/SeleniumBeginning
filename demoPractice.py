import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
list = []
veggieList = []
driver = webdriver.Chrome(executable_path="driver/chromedriver-3")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")
time.sleep(3)
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
print(count)
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    list.append(button.find_element(By.XPATH, "parent::div/parent::div/h4"))
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
# //span[@class='totAmt']
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
totalAmnt1 = driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text
print(totalAmnt1)
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, " .promoBtn").click()
# wait = WebDriverWait(driver, 5)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "promoCode")))
# totalAmnt2 = driver.find_element(By.CSS_SELECTOR, "span[class='totAmt']").text
# print(totalAmnt2)

Veggies = driver.find_elements(By.XPATH, "//tr/td[2]/p")
for v in Veggies:
    veggieList.append(v.text)
print(veggieList)

sum = 0
TotalAmount = driver.find_elements(By.XPATH, "//tr/td[5]/p")
for veggieTotal in TotalAmount:
    sum = sum + int(veggieTotal.text)

print(sum)
assert sum == int(totalAmnt1)

