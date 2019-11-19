# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(firstname='Aliaksandr', middlename='Igorevich', lastname='Kuzmitski',
                                       nickname='technodeath', photo='E:\\1332955017586.jpg', title='QA',
                                       company='ScienceSoft', address='No address', home='No home', mobile='No',
                                       work='No work', fax='No fax', email='No email1', email2='No email2',
                                       email3='No email3', homepage='No homepage', bday='1', bmonth='September',
                                       byear='1941', aday='9', amonth='May', ayear='1945', address2='TestAddress',
                                       phone2='Test phone2', notes='test note')
    app.contact.press_add_new_contact()
    app.contact.fill_contact_info(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    print(old_contacts)
    old_contacts.append(contact)
    print(old_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
