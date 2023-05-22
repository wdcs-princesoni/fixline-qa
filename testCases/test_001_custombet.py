from pageObjects.HomePageObject import HomePage
from pageObjects.MetaMaskObject import MetaMask
from pageObjects.CreateBetObject import CreateBet

class TestBetCreate:

    def test_create_bet(self, driver_setup):
        self.driver = driver_setup
        self.driver.get("https://fixline-staging.codezeros.com")
        hp = HomePage(self.driver)
        mm = MetaMask(self.driver)
        cb = CreateBet(self.driver)
        hp.connect_wallet()
        #
        cb.create_custom_bet("ABc", "asd", "assd")


