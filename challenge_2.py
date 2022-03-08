from selenium import webdriver

chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_elements_by_css_selector(".mp-bordered a")
content = []

for i in count:
    content.append(i.text)

print(content[4])


count_2 = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
print(count_2.text)


driver.quit()