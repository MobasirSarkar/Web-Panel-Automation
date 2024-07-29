# from selenium import webdriver
from selenium.webdriver.common.by import By
from Panels.view_manage.branchManage import BranchManage
import time


class ViewManage:
    def __init__(self, driver):
        self.driver = driver

    def viewManagePanel(self):
        driver = self.driver
        view_manage_btn = driver.find_element(
            By.XPATH, "//*[@id='sidenavAccordion']/div/div/a[6]"
        )
        view_manage_btn.click()
        brMang = BranchManage(driver)
        brMang.branch()
        time.sleep(1)
