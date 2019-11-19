from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_login_page(self):
        # open login
        wd = self.wd
        if not ((wd.current_url == "http://localhost/addressbook/") and len(wd.find_elements_by_xpath("//input[@value='Login']")) > 0):
            wd.get("http://localhost/addressbook/")

    def open_home_page(self):
        # open home page
        wd = self.wd
        if not ((wd.current_url == "http://localhost/addressbook/") and len(wd.find_elements_by_xpath("//input[@type='button' and @value='Send e-Mail']")) > 0):
            wd.find_element_by_xpath("//a[text()='home']").click()

    def destroy(self):
        self.wd.quit()