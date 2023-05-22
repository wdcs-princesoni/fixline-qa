from pageObjects.HomePageObject import HomePage
from pageObjects.MetaMaskObject import MetaMask
from pageObjects.CreateBetObject import CreateBet
import os
from utilities import QuestionGenerator

class TestBetCreate:

    def test_create_bet(self, driver_setup):
        self.driver = driver_setup
        self.driver.get("https://fixline-staging.codezeros.com")
        home_page = HomePage(self.driver)
        wallet = MetaMask(self.driver)
        custom_bet = CreateBet(self.driver)
        home_page.connect_wallet()
        #
        result = custom_bet.create_custom_bet(QuestionGenerator.ques,QuestionGenerator.one, QuestionGenerator.two)
        if result is True:
            assert True
        else:
            self.driver.save_screenshot(os.getcwd() + "//screenshots" + "test_001_custom_bet")
            assert False


