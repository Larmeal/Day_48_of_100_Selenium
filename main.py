from selenium import webdriver

chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("https://www.python.org")

time_events = driver.find_elements_by_css_selector(".event-widget time")
work_events = driver.find_elements_by_css_selector(".event-widget li a")
event = {}

for i in range(len(time_events)):
    event[i + 1] = {
        "time": time_events[i].text,
        "name": work_events[i].text
    }

driver.quit()