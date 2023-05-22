from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# from selenium import  webdriver

class MetaMask:
    txt_password_metamask = (By.ID, "password")
    btn_unlock = (By.XPATH, "//button")
    text_password = "Metamask@123"
    btn_confirm = (By.XPATH, "//button[text()='Confirm']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def unlock_metamask(self):
        # print(self.driver.current_handle)
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        # print(self.driver.current_handle)

        pwd = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        pwd.send_keys(*MetaMask.text_password)
        self.driver.find_element(*MetaMask.btn_unlock).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        # print(self.driver.current_handle)

    def confirm_transaction(self):
        # self.driver = webdriver.Chrome()
        self.wait.until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        confirm = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Confirm']")))
        confirm.click()
        self.driver.switch_to.window(self.driver.window_handles[0])



