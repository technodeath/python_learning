# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if db.get_contact_list() == 0:
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(Contact(firstname='Aliaksandr', middlename='Igorevich', lastname='Kuzmitski',
                                       nickname='technodeath', photo='E:\\1332955017586.jpg', title='QA',
                                       company='ScienceSoft', address='No address', home='No home', mobile='No',
                                       work='No work', fax='No fax', email='No email1', email2='No email2',
                                       email3='No email3', homepage='No homepage', bday='1', bmonth='September',
                                       byear='1941', aday='9', amonth='May', ayear='1945', address2='TestAddress',
                                       phone2='Test phone2', notes='test note'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id)
    app.contact.fill_contact_info_update(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
