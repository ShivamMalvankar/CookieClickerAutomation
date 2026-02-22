from time import sleep, time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

url = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
sleep(3)
try:
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

sleep(2)


cookie = driver.find_element(By.ID, value='bigCookie')

wait_time = 5
timeout = time() + wait_time
five_min = time() + 60 * 5

while True:
    cookie.click()

    if time() > timeout:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            cookie_text = cookies_element.text
            cookie_count = cookie_text.split()[0].replace(",", "")
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            best_item = None
            for product in reversed(products):
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    print(f"brought item {best_item.get_attribute('id')}")
                    upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
                    most_expensive_upgrades_index = len(upgrades) - 1
                    most_expensive_upgrade = driver.find_element(By.ID, value=f"product{most_expensive_upgrades_index}")
                    most_expensive_upgrade.click()

        except (NoSuchElementException, ValueError):
            print("couldn't find cookie count or items.")

        timeout = time() + wait_time

    if time() > five_min:
        try:
            cookies_element = driver.find_element(By.ID, value="cookies")
            print(f"final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't find element.")
        break
