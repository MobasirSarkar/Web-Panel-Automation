# from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LogOut:

    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        log_out_driver = self.driver
        # logging out
        log_out_driver.implicitly_wait(2)
        log_out_select = log_out_driver.find_element(
            By.XPATH, "/html/body/div/div[1]/nav/div/div/a[8]"
        )
        log_out_driver.execute_script(
            "arguments[0].scrollIntoView(true);", log_out_select
        )
        time.sleep(1)
        log_out_select.click()
