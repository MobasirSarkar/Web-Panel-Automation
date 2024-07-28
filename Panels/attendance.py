from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Attendance:
    def __init__(self, driver):
        self.driver = driver

    def attendance(self, emp_name_input):
        self.driver.implicitly_wait(2)
        attendance = self.driver.find_element(
            By.XPATH, "//*[@id='sidenavAccordion']/div/div/a[2]"
        )
        attendance.click()

        # date filter
        self.driver.implicitly_wait(2)
        date_filter = self.driver.find_element(By.XPATH, "//*[@id='startDated']/span")
        date_filter.click()
        clear_btn = self.driver.find_element(
            By.XPATH, "/html/body/div[4]/div[4]/button[1]"
        )
        clear_btn.click()
        self.driver.implicitly_wait(2)
        date_filter.click()
        start_date = self.driver.find_element(
            By.XPATH, "/html/body/div[4]/div[2]/div[1]/table/tbody/tr[1]/td[2]"
        )
        start_date.click()
        self.driver.implicitly_wait(1)
        end_date = self.driver.find_element(
            By.XPATH, "/html/body/div[4]/div[2]/div[1]/table/tbody/tr[4]/td[5]"
        )
        end_date.click()
        self.driver.implicitly_wait(1)
        apply_btn = self.driver.find_element(By.CLASS_NAME, "applyBtn")
        time.sleep(2)
        apply_btn.click()

        # employee name
        input = emp_name_input
        emp_name = self.driver.find_element(By.ID, "empname")
        emp_name.send_keys(input)

        # search
        search_btn = self.driver.find_element(
            By.XPATH, "//*[@id='attendancesearch']/div[2]/div[4]/button"
        )
        search_btn.click()
        time.sleep(2)

        # download reports
        download_opt = Select(self.driver.find_element(By.ID, "export"))
        download_opt.select_by_value("PDF")
        download_btn = self.driver.find_element(
            By.XPATH, "//*[@id='attendSubHeaderancesearch']/div/div[1]/div[11]/a/button"
        )
        download_btn.click()
        time.sleep(2)
