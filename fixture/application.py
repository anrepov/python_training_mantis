from selenium import webdriver

from fixture.navigation import NavigationHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome("../drivers/chromedriver.exe")
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unknown browser %s" % browser)
        self.session = SessionHelper(self)
        self.navigation = NavigationHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
