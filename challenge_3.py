from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element_by_name("fName") 
first_name.send_keys("abcde")

last_name = driver.find_element_by_name("lName") 
last_name.send_keys("abcde")

email = driver.find_element_by_name("email") 
email.send_keys("abcde@gmail.com")

button = driver.find_element_by_css_selector("form button")
button.click()