import time
from selenium import webdriver

chrome_driver_path = "/path/to/your/driver"
browser = webdriver.Chrome(executable_path=chrome_driver_path)

browser.get("http://orteil.dashnet.org/experiments/cookie/")
cookies = browser.find_element_by_id("cookie")
items_div = browser.find_elements_by_css_selector("#store div")
items_id = [item.get_attribute("id") for item in items_div]

checking_time = time.time() + 5
while True:
    cookies.click()

    if time.time() > checking_time:
        all_prices = browser.find_elements_by_css_selector("#store b")
        item_prices = [int(price.text.split("-")[1].replace(",", "").strip()) for price in all_prices if price.text != ""]
        money = int(browser.find_element_by_id("money").text.replace(",", "").strip())
        affordable_items_dict = {items_id[i]: item_prices[i] for i in range(len(item_prices)) if money >= item_prices[i]}
        max_item_price = max(list(affordable_items_dict.values()))
        max_item_id = list(affordable_items_dict.keys())[list(affordable_items_dict.values()).index(max_item_price)]
        buy = browser.find_element_by_id(max_item_id).click()
        checking_time += 5
