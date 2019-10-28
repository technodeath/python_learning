from selenium import webdriver

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def go_to_groups_page(self):
        # go to groups page
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def fill_and_submit_new_group(self, group):
        # fill the group form and submit
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.go_to_groups_page()

    def create_new_group(self):
        # press "new group"
        wd = self.wd
        self.open_groups()
        wd.find_element_by_name("new").click()

    def open_groups(self):
        # press "groups" menu item
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        # enter credentials and login
        wd = self.wd
        self.open_login_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self):
        # open login
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()