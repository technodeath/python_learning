from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_info(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_photo_value(self, field_name, photo_path):
        wd = self.app.wd
        if photo_path is not None:
            wd.find_element_by_name(field_name).send_keys(photo_path)

    def change_birthday_value(self, field_name, birthday):
        wd = self.app.wd
        if birthday is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(birthday)
            wd.find_element_by_name(field_name).click()

    def fill_contact_form(self, contact):
        # fill all contact info and upload the image
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_photo_value("photo", contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_birthday_value("bday", contact.bday)
        self.change_birthday_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_birthday_value("aday", contact.aday)
        self.change_birthday_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def fill_contact_info_update(self, contact):
        # fill all contact info and upload the image
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()

    def press_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select 1st
        self.app.open_login_page()
        wd.find_element_by_name("selected[]").click()
        # click "delete"
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to.alert.accept()
        self.app.open_login_page()

    def edit_first_contact(self):
        wd = self.app.wd
        # select 1st contact
        self.app.open_login_page()
        wd.find_element_by_name("selected[]").click()
        # click "edit"
        wd.find_elements_by_css_selector('a[href^="edit.php?id"]')[0].click()

    def count(self):
        wd = self.app.wd
        self.app.open_login_page()
        return len(wd.find_elements_by_name("selected[]"))
