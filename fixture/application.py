from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
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
        if not wd.current_url == "http://localhost/addressbook/":
            wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()