# -*- coding: utf-8 -*-
from selenium import webdriver
from group import Group
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddGroupTestcase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group_testcase(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_groups(wd)
        self.create_new_group(wd)
        self.fill_and_submit_new_group(wd, Group(name='test name', header='test header', footer='test footer'))
        self.go_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_group_testcase(self):
        wd = self.wd
        self.open_login_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_groups(wd)
        self.create_new_group(wd)
        self.fill_and_submit_new_group(wd, Group(name='', header='', footer=''))
        self.go_to_groups_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def go_to_groups_page(self, wd):
        # go to groups page
        wd.find_element_by_link_text("group page").click()

    def fill_and_submit_new_group(self, wd, group):
        # fill the group form and submit
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

    def create_new_group(self, wd):
        # press "new group" button
        wd.find_element_by_name("new").click()

    def open_groups(self, wd):
        # press "groups" menu item
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, username, password):
        # enter credentials and login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_login_page(self, wd):
        # open login page
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
