import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Path="./chromedriver.exe"

driver=webdriver.Chrome(Path)
driver.get("https://techwithtim.net/")
time.sleep(5)
search=driver.find_element_by_css_selector("input[class='search-field']")
search.sendKeys("Test")
search.sendKeys(Keys.RETURN)
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    articles = main.find_element_by_id

finally:
    driver.close()

