class GroupHelper:

    def __init__(self, app):
        self.app = app

    def go_to_groups_page(self):
        # go to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_and_submit_new_group(self, group):
        # fill the group form and submit
        wd = self.app.wd
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

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        # select 1st group
        wd.find_element_by_name("selected[]").click()
        # click "delete"
        wd.find_element_by_name("delete").click()
        self.open_groups()

    def create(self):
        # press "new group"
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("new").click()

    def open_groups(self):
        # press "groups" menu item
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()