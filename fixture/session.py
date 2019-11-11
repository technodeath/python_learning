class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        # enter credentials and login
        wd = self.app.wd
        self.app.open_login_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        # logout
        wd = self.app.wd
        wd.find_element_by_xpath("//a[text()='Logout']").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[text()='Logout']")) > 0

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//a[text()='Logout']/preceding-sibling::b").text == "("+username+")"


