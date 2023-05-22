from selenium import webdriver
import pytest


@pytest.fixture()
def driver_setup():
    options = webdriver.FirefoxOptions()
    options.binary_location = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    options.add_argument("--profile")
    options.add_argument("C:/Users/Dell/AppData/Roaming/Mozilla/Firefox/Profiles/hruu8oux.default-release-1683791912031")
    driver = webdriver.Firefox(options=options)

    return driver
