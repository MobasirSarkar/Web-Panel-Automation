import random, time
from selenium.webdriver.common.by import By

# from selenium import webdriver
from selenium.webdriver.support.ui import Select


class BranchMange:
    def __init__(self, driver):
        self.driver = driver

    def branch(self):

        # click on the branch section
        branch_select = self.driver.find_element(
            By.XPATH, "//*[@id='collapseLayouts']/nav/a[1]"
        )
        branch_select.click()
        self.driver.implicitly_wait(2)
        # create branch

        add_branch_btn = self.driver.find_element(By.ID, "linkBtn")
        add_branch_btn.click()
        self.driver.implicitly_wait(1)
        branch_code = self.driver.find_element(By.ID, "branch_code")
        branch_code_gen = f"branch{str(random.randint(0,9))}"
        branch_code.send_keys(branch_code_gen)

        # select country
        self.driver.find_element(By.ID, "country-dropdown").click()
        self.driver.implicitly_wait(1)
        select_country = Select(self.driver.find_element(By.ID, "country-dropdown"))
        select_country.select_by_value("101")

        # select state
        self.driver.find_element(By.ID, "state-dropdown").click()
        self.driver.implicitly_wait(1)
        select_state = Select(self.driver.find_element(By.ID, "state-dropdown"))
        select_state.select_by_value("13")

        # select city
        self.driver.find_element(By.ID, "city-dropdown").click()
        self.driver.implicitly_wait(1)
        select_city = Select(self.driver.find_element(By.ID, "city-dropdown"))
        select_city.select_by_value("1126")

        # enter address
        address = self.driver.find_element(By.ID, "address")
        address.send_keys("Delhi")
        self.driver.implicitly_wait(1)

        # enter lat and long
        lat = self.driver.find_element(By.ID, "lat")
        lat.send_keys("28.3938310")
        self.driver.implicitly_wait(1)
        long = self.driver.find_element(By.ID, "lng")
        long.send_keys("77.0324410")

        # geofencing
        geo_fec = self.driver.find_element(By.ID, "geofencing")
        geo_fec.send_keys("1")

        # add button
        add_button = self.driver.find_element(
            By.XPATH, "//*[@id='branchId']/div/div[2]/button"
        )
        add_button.click()
        time.sleep(3)

        # search branch by code
        try:
            code_input = self.driver.find_element(By.ID, "branchcode")
            code_input.send_keys(branch_code_gen)
        except Exception as e:
            print(e)
        search_btn = self.driver.find_element(
            By.XPATH, "//*[@id='branchsearch']/div/div[6]/button"
        )
        search_btn.click()
        time.sleep(2)
