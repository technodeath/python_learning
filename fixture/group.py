class GroupHelper:

    def __init__(self, app):
        self.app = app

    def go_to_groups_page(self):
        # go to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def fill_and_submit_new_group(self, group):
        # fill the new group form and submit
        wd = self.app.wd
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        self.go_to_groups_page()

    def fill_and_submit_edit_group(self, group):
        # fill the group form and submit
        wd = self.app.wd
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.go_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        # click "delete"
        wd.find_element_by_name("delete").click()
        self.open_groups()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def edit_first_group(self):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        # click "edit"
        wd.find_element_by_name("edit").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.go_to_groups_page()

    def create(self):
        # press "new group"
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("new").click()

    def open_groups(self):
        # press "groups" menu item
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath('//h1[text() = "Groups"]')