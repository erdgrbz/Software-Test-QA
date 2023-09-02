from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

#Frontend Case with Selenium on Python
driver = webdriver.Chrome()
driver.get("https://flights-app.pages.dev/")

#Same Flight
try:
        from_combobox = driver.find_element(By.ID, 'headlessui-combobox-input-:Rq9lla:')
        from_combobox.send_keys("Paris")
        from_combobox.send_keys(Keys.ENTER)
        time.sleep(1)

        to_combobox = driver.find_element(By.ID, 'headlessui-combobox-input-:Rqhlla:')
        to_combobox.send_keys("Paris")
        to_combobox.send_keys(Keys.ENTER)

        selected_from = from_combobox.get_attribute("value")
        selected_to = to_combobox.get_attribute("value")

finally:
        if selected_from == selected_to:
            print("\nError! 'From' and 'To' inputs are the same.")
        else:
            print("\n'From' and 'To' inputs are different.")
        driver.quit()

#Amount of Flights
try:
        time.sleep(1)
        driver = webdriver.Chrome()
        driver.get("https://flights-app.pages.dev/")

        from_combobox = driver.find_element(By.ID, 'headlessui-combobox-input-:Rq9lla:')
        from_combobox.send_keys("Istanbul")
        from_combobox.send_keys(Keys.ENTER)
        time.sleep(1)

        to_combobox = driver.find_element(By.ID, 'headlessui-combobox-input-:Rqhlla:')
        to_combobox.send_keys("Los Angeles")
        to_combobox.send_keys(Keys.ENTER)
        time.sleep(1)

        flights = driver.find_elements(By.XPATH, "/html/body/main/div[2]/div/ul/li")
        flight_count = len(flights)
        print("\nNumber of flights:", flight_count)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        found_items = soup.find('p', class_='mb-10').text
        print(found_items)

        number = int(found_items.split()[-2])

        if number == flight_count:
            print("\nText and flights shown are same.")
        else:
            print("\nText and flights shown are not same.")

finally:
        driver.quit()

