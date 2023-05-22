import os
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
from pageObjects.MetaMaskObject import MetaMask

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateBet:
    btn_create_bet = (By.XPATH, "//button[@title='Create a Bet']")
    btn_custom_bet = (By.XPATH, "//div[@class='btn-content'][normalize-space()='Custom']")
    txt_question = (By.XPATH, "//textarea")
    txt_ans_one = (By.XPATH, "(//input[@placeholder='Type answer choice...'])[1]")
    txt_ans_two = (By.XPATH, "(//input[@placeholder='Type answer choice...'])[2]")
    rd_category = (By.XPATH, "//div[@id='depwithTainer'][3]//div[@class='row']//label")  # Returns the list
    rd_picture_on_card = (By.XPATH, "//div[@id='depwithTainer'][4]//div[@class='row']//label")  # Returns the list.
    btn_next = (By.XPATH, "//div[@id='launch-accordion']//button[@type='button']")
    btn_confirm_matic = (By.XPATH, "//div[@id='options-accordion']//button[@type='button']")
    lbl_success = (By.XPATH, "//div[@data-testid='toast-content']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.mm = MetaMask(self.driver)

    def create_custom_bet(self, que, a_one, a_two):
        # self.driver = webdriver.Chrome()
       try:
            time.sleep(3)
            plus = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Create a Bet']")))#find_element(*CreateBet.btn_create_bet)  # Performed click action through Actionchains.
            ActionChains(driver=self.driver).click(plus).perform()
            self.driver.find_element(*CreateBet.btn_custom_bet).click()
            self.driver.find_element(*CreateBet.txt_question).send_keys(que)
            self.driver.find_element(*CreateBet.txt_ans_one).send_keys(a_one)
            self.driver.find_element(*CreateBet.txt_ans_two).send_keys(a_two)
            category = self.driver.find_elements(*CreateBet.rd_category)
            category[(random.randint(0, 2))].click()
            picture = self.driver.find_elements(*CreateBet.rd_picture_on_card)
            picture[(random.randint(0, 2))].click()
            self.driver.find_element(*CreateBet.btn_next).click()
            self.driver.find_element(*CreateBet.btn_confirm_matic).click()
            self.mm.confirm_transaction()
            success = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='toast-content']")))
            if success.is_displayed():
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@data-testid='toast-content']")))
                self.driver.quit()
                return True
            else:
                self.driver.quit()
                return False
       except:
           return False
