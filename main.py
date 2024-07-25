from config import Config
from login.login import Login
import time


def main():
    url = Config.BASE_URl
    code = Config.ORG_CODE
    userId = Config.USERID
    mPin = Config.MPIN

    web_driver = Login(url, code, userId, mPin)
    web_driver.run()


if __name__ == "__main__":
    main()
