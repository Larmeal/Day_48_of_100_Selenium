from selenium import webdriver
import time

chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

TIME_STACK = 0
TIME_UP = 1000
GAME_OVER = True
ORDER_BUY = ["buyTime machine", "buyPortal", "buyAlchemy lab", "buyShipment", "buyMine", "buyFactory", "buyGrandma", "buyCursor"]
PRICE = []

def price():
    for i in range(len(ORDER_BUY)):
        try:
            order = driver.find_elements_by_xpath(f'//*[@id="{ORDER_BUY[i]}"]/b')
            PRICE.append(order[0].text.split()[3])
        except IndexError:
            PRICE.append(order[0].text.split()[2])
        
    for i in PRICE:
        text = [char for char in i]
        text_reverse = text[::-1]
        if len(i) > 8:
            if text_reverse[3] == ",":
                edit = PRICE[PRICE.index(i)].replace(",", "")
                PRICE.insert(PRICE.index(i), edit)
                PRICE.pop(PRICE.index(i))
        else:
            try:
                if text_reverse[3] == ",":
                    edit = PRICE[PRICE.index(i)].replace(",", "")
                    PRICE.insert(PRICE.index(i), edit)
                    PRICE.pop(PRICE.index(i))
            except IndexError:
                pass


def click_ability():
    for i in range(len(ORDER_BUY)):
        if int(PRICE[i]) <= COOKIE:
            driver.find_element_by_xpath(f'//*[@id="{ORDER_BUY[i]}"]/b').click()
    

while GAME_OVER:
    time.sleep(0)
    COOKIE = int(driver.find_element_by_css_selector("#money").text)
    print(COOKIE)

    price()
    click_ability()

    if TIME_STACK != TIME_UP:
        TIME_STACK += 1
        button = driver.find_element_by_css_selector("#cookie")
        button.click()
        PRICE = []
        
        
    elif TIME_STACK == TIME_UP:
        GAME_OVER = False


driver.quit()