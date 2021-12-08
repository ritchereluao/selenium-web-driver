from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("DRIVER LOCATION")
driver = webdriver.Chrome(service=service)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # # To click on the article link
# # article_count.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# # search.send_keys("Python")
# # search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("First")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Last II")

email = driver.find_element(By.NAME, "email")
email.send_keys("emailaddress@gmail.com")

# submit = driver.find_element(By.XPATH, '/html/body/form/button')
submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()
