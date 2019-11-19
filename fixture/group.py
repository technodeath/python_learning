from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def go_to_groups_page(self):
        # go to groups page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
            wd.find_element_by_xpath('//h1[text() = "Groups"]')

    def fill_and_submit_new_group(self, new_group_data):
        # fill the new group form and submit
        wd = self.app.wd
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("submit").click()
        self.go_to_groups_page()
        self.group_cache = None

    def fill_and_submit_edit_group(self, new_group_data):
        # fill the group form and update
        wd = self.app.wd
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        self.go_to_groups_page()
        self.group_cache = None

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
        self.group_cache = None

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
        self.group_cache = None

    def create(self):
        # press "new group"
        wd = self.app.wd
        self.open_groups()
        wd.find_element_by_name("new").click()

    def open_groups(self):
        # press "groups" menu item
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()
            wd.find_element_by_xpath('//h1[text() = "Groups"]')

    def count(self):
        wd = self.app.wd
        self.open_groups()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_groups_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
