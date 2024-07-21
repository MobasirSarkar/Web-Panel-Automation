from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


class Login:
    def __init__(self, url, code):
        self.url = url
        self.code = code
        self.web_driver = None

    def login(self):

        # Initial panel
        web_driver = webdriver.Chrome()
        web_driver.implicitly_wait(10)
        web_driver.get(self.url)
        byi = By.ID
        byx = By.XPATH

        # organization code panel
        org_code = web_driver.find_element(byi, "passcode")
        org_code.send_keys(self.code)
        org_code.send_keys(Keys.RETURN)
        time.sleep(2)

        # continue_panel
        web_driver.implicitly_wait(2)
        con_panel = web_driver.find_element(
            byx, "//*[@id='companySelModal']/div/div/div/div[2]/div/button"
        )
        con_panel.click()

        # user_id
        user_id = web_driver.find_element(byi, "userid")
        user_id.send_keys("instamobasir23@gmail.com")
        time.sleep(2)

        # org_selection
        org_select_click = web_driver.find_element(byi, "role_name")
        org_select_click.click()
        time.sleep(4)
        org_select = Select(web_driver.find_element(byi, "role_name"))
        org_select.select_by_value("2")
        time.sleep(1)

        # user_mpin
        mpin = web_driver.find_element(byi, "digit")
        mpin.send_keys("1")

        for i in range(2, 5):
            values = f"digit-{i}"
            mpin2 = web_driver.find_element(byi, values)
            mpin2.send_keys("1")

        # login_button
        log_btn = web_driver.find_element(byi, "submitBtn")
        log_btn.click()

        # driver quit
        time.sleep(4)
        web_driver.quit()

    def run(self):
        Login.login(self)