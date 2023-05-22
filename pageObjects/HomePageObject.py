from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.MetaMaskObject import MetaMask


class HomePage:
    btn_connect_wallet = (By.XPATH, "//*[@id='titlebar']//button[1]//span")
    btn_metamask = (By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[2]/button[1]")

    def __init__(self, driver):
        self.driver = driver
        self.obj_mm = MetaMask(self.driver)
        self.wait = WebDriverWait(self.driver, 20)

    def connect_wallet(self):
        # if "Connect" in self.driver.find_element(*HomePage.btn_connect_wallet).text:
            wallet = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@title='Connect your wallet']")))

            wallet.click()

            mm = self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//body[1]/div[3]/div[1]/div[1]/div[2]/button[1]")))
            mm.click()
            # self.driver.find_element(*HomePage.btn_connect_wallet).click()
            # self.driver.find_element(*HomePage.btn_metamask).click()
            self.obj_mm.unlock_metamask()
        # elif "0x" in self.driver.find_element(*HomePage.btn_connect_wallet).text:
        #     pass
        # else:
        #     try:
        #         # self.driver = webdriver.Chrome
        #         alert = self.driver.switch_to.alert
        #         alert.accept()
        #         self.driver.find_element(*HomePage.btn_connect_wallet).click()
        #         self.driver.find_element(*HomePage.btn_metamask).click()
        #     except Exception as err:
        #         print(err, "Something went wrong")
