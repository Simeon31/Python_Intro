from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://github.com")

signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username = browser.find_element(By.ID, "login_field")
password = browser.find_element(By.ID, "password")

username.send_keys("MasterCoder14")
password.send_keys("today_is_almost_over")
password.submit()