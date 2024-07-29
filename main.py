from selenium import webdriver
from Panels.attendance import Attendance
from Panels.devicegate import DeviceGate
from Panels.logout import LogOut
from Panels.view_manage.run import ViewManage
from config import Config
from login.login import Login
import time, random


def main():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = Config.BASE_URl
    code = Config.ORG_CODE
    userId = Config.USERID
    mPin = Config.MPIN

    login = Login(url, code, userId, mPin, driver)
    login.run()
    time.sleep(1)
    attendace = Attendance(driver)
    attendace.attendance("abdul")
    time.sleep(1)
    gate_name = str(random.randint(0, 9))
    gate_id = str(random.randint(1111, 2000))
    device_gate_panel = DeviceGate(driver)
    device_gate_panel.gatedevice("778", gate_name, gate_id)
    viewManage = ViewManage(driver)
    viewManage.viewManagePanel()
    logout = LogOut(driver)
    logout.logout()
    driver.quit()


if __name__ == "__main__":
    main()
