from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://cv.ee/et/')

# marksonad = driver.find_element_by_xpath('//*[@id="react-select-2-input"]')
# marksonad = driver.find_element_by_id('react-select-2-input')
marksonad = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div/div[3]/form/div[1]/div/div[3]/div/div/div[1]/div[2]/div/input')
marksonad.send_keys('PYTHON')
buttonOtsi = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div/div/div[3]/form/div[3]/footer/span/button')
buttonOtsi.send_keys(Keys.RETURN)
source1 = driver.page_source
print(source1)

