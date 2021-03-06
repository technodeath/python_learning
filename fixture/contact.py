from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_info(self, contact):
        wd = self.app.wd
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.app.open_home_page()
        self.contact_cache = None

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
        self.contact_cache = None

    def press_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def add_to_group_by_group_id(self, id):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(str(id))
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_name("add").click()
        wd.get('http://localhost/addressbook')  # here is a bug in the app - avoid it

    def delete_from_group_by_contact_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//h1[text()='Delete record']")
        self.app.open_home_page()

    def select_group_to_view_by_group_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("select[name='group']").click()
        Select(wd.find_element_by_css_selector("select[name='group']")).select_by_value(str(id))
        wd.find_element_by_css_selector("select[name='group']").click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click "delete"
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//h1[text()='Delete record']")
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//h1[text()='Delete record']")
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_from_group_by_id(self, id):
        wd = self.app.wd
        self.select_contact_by_id(id)
        wd.find_element_by_name("remove").click()
        wd.switch_to.alert.accept()
        wd.find_element_by_xpath("//h1[text()='Delete record']")
        self.app.open_home_page()

    def edit_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # click "edit"
        wd.find_element_by_css_selector('a[href^="edit.php?id"]').click()

    def edit_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click "edit"
        wd.find_elements_by_css_selector('a[href^="edit.php?id"]')[index].click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # click "view"
        wd.find_elements_by_css_selector('a[href^="view.php?id"]')[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_in_group(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.app.contact.select_group_to_view_by_group_id(group_id)
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                lastname = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(3)").text
                address = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(4)").text
                id = element.find_element_by_css_selector("input[name='selected[]']").get_attribute("value")
                all_emails = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(5)").text
                all_phones = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(6)").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, address=address, id=id,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def diff(self, li1, li2):
        return list(set(li1) - set(li2))

    def get_contacts_list_vs_db(self, group_id):
        if self.contact_cache is None:
            wd = self.app.wd
            wd.get('http://localhost/addressbook/?group=%s') % group_id
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                lastname = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("tr[name='entry']>td:nth-child(3)").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")

        return (Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                        home=homephone, phone2=secondaryphone, work=workphone, mobile=mobilephone,
                        email=email, email2=email2, email3=email3))

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return (Contact(home=homephone, phone2=secondaryphone,
                        work=workphone, mobile=mobilephone))



