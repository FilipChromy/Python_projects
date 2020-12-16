from selenium import webdriver

url = "https://orteil.dashnet.org/cookieclicker/"
driver = webdriver.Chrome()
driver.get(url)

clickable_cookie = driver.find_element_by_id("bigCookie")

while True:
    clickable_cookie.click()    
    try:
        upgrade = driver.find_element_by_class_name("unlocked.enabled")
        upgrade.click()
    except:
        print("Element not found")