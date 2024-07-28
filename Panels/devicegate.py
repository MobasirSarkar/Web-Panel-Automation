from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.ui import Select
import time

# from selenium import webdriver


class DeviceGate:

    def __init__(self, driver):
        self.driver = driver

    def gatedevice(self, branch_id, gatename, gateid):
        # Device_Gate
        dev_gate_link = self.driver.find_element(
            By.XPATH, "//*[@id='sidenavAccordion']/div/div/a[4]"
        )
        dev_gate_link.click()

        # Add gate
        self.driver.implicitly_wait(2)
        add_gate = self.driver.find_element(By.XPATH, "//*[@id='linkBtn']")
        add_gate.click()
        self.driver.find_element(By.ID, "branch_id").click()
        branch_select = Select(self.driver.find_element(By.ID, "branch_id"))
        self.driver.implicitly_wait(1)
        branch_select.select_by_value(branch_id)
        gate_name = self.driver.find_element(By.ID, "gatname")
        gate_name.send_keys(gatename)
        self.driver.implicitly_wait(1)
        gate_id = self.driver.find_element(By.ID, "gatid")
        gate_id.send_keys(gateid)
        gate_btn = self.driver.find_element(
            By.XPATH, "//*[@id='addGate']/div/div[3]/button"
        )
        gate_btn.click()
        time.sleep(3)
        se_gate_id = self.driver.find_element(By.ID, "gateid")
        se_gate_id.send_keys(gateid)
        search_gate = self.driver.find_element(
            By.XPATH, "//*[@id='gateSearch']/div/div[3]/button"
        )
        search_gate.click()
        time.sleep(2)

        # Add device
        device_select = self.driver.find_element(
            By.XPATH,
            "//*[@id='layoutSidenav_content']/main/div/div/div[2]/div/ul/li[2]/button/a",
        )
        device_select.click()
        add_device = self.driver.find_element(By.ID, "linkBtn2")
        add_device.click()
        self.driver.implicitly_wait(1)
        self.driver.find_element(By.ID, "device_branchId").click()
        select_branch = Select(self.driver.find_element(By.ID, "device_branchId"))
        select_branch.select_by_value(branch_id)
        device_name = self.driver.find_element(By.ID, "device_name")
        device_name_gen = f"mobile{str(random.randint(0,9))}"
        device_name.send_keys(device_name_gen)
        device_imei = self.driver.find_element(By.ID, "imei")
        device_imei_gen = str(random.randint(11111111, 99999999))
        device_imei.send_keys(device_imei_gen)
        self.driver.implicitly_wait(1)
        dev_id = str(random.randint(1000, 2000))
        device_id = self.driver.find_element(By.ID, "deviceId")
        device_id.send_keys(dev_id)
        self.driver.implicitly_wait(2)
        add_device_btn = self.driver.find_element(
            By.XPATH, "//*[@id='addDevice']/div/div[3]/button"
        )
        add_device_btn.click()
        time.sleep(2)
        se_device_id = self.driver.find_element(By.ID, "devid")
        se_device_id.send_keys(dev_id)
        search_device_btn = self.driver.find_element(
            By.XPATH, "//*[@id='getsearchDevice']/div/div[3]/button"
        )
        self.driver.implicitly_wait(2)
        search_device_btn.click()
        time.sleep(2)
