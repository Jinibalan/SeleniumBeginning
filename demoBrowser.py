from selenium import webdriver

driver = webdriver.Chrome(executable_path="driver/chromedriver-3")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  #get method to hit url on  browser

print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()




