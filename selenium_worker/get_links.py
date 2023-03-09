from selenium_worker.create_selenium import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


def get_mobile_link() -> str:
    driver.get('https://suchen.mobile.de/fahrzeuge/search.html?s=Truck&vc=TruckOver7500')
    time.sleep(1)

    driver.find_element(By.CLASS_NAME, 'mde-consent-accept-btn').click()  # accept all cookes

    if search_config.vehicle_condition == 'Neu':
        driver.find_element(By.ID, 'usage-NEW-ds').click()
    else:
        driver.find_element(By.ID, 'usage-USED-ds').click()

    Select(driver.find_element(By.XPATH, f'//*[@id="categories-ds"]')).select_by_value(search_config.vehicle_category)
    Select(driver.find_element(By.XPATH, '//*[@id="selectMake1-ds"]')).select_by_visible_text(search_config.vehicle_brand)
    driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]').click()

    return driver.current_url
