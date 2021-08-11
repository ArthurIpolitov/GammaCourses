from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
driver.get('https://particle-clicker.web.cern.ch/')

click_object = driver.find_element_by_id('detector-events')

actions = ActionChains(driver)
actions.click(click_object)
count = 0

for i in range(500):
    actions.perform()



# link = driver.find_element_by_link_text('Rohkem infot')
# link.click()

# link2 = driver.find_element_by_xpath('//*[@id="hp"]/div[1]/div[3]/div[1]/p[2]/a')
# link2.click()
# source1 = driver.page_source
# time.sleep(5)
# driver.back()
# source2 = driver.page_source
# if source2 == source1:
#     print('same')
# else:
#     print('not same')

# element = driver.find_elements_by_tag_name('td')
# print(element)
# for el in element:
#     print(el.text)


# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(By.ID, 'user_email'))
# except:
#     print('Error')
# finally:
#     driver.quit()

# search = driver.find_element_by_name('q')
# search.send_keys('python')
# search.send_keys(Keys.RETURN)
# print(search.is_enabled())
# print(search.is_selected())
# print(search.is_displayed())

# email_input = driver.find_element_by_id('user_email')
# email_input.send_keys('artur.ipolitov2@gmail.com')
# button_sign = driver.find_element_by_xpath("/html/body/div[4]/main/div[1]/div[1]/div[1]/div/div/div[1]/form/div/button")
# button_sign.click()
#
# button_cont = driver.find_element_by_class_name('signup-continue-button')
# time.sleep(10)
# button_cont.click()
# password_input = driver.find_element_by_id('password')
# password_input.send_keys('somepasswordfortest123456')
# password_input.send_keys(Keys.RETURN)
# time.sleep(5)
# next_button = driver.find_element_by_xpath('//*[@id="password-container"]/div[2]/button')
# next_button.click()
