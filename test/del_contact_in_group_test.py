# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_random_contact_from_random_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.fill_contact_info(Contact(firstname='Aliaksandr', middlename='Igorevich', lastname='Kuzmitski',
                                       nickname='technodeath', photo='E:\\1332955017586.jpg', title='QA',
                                       company='ScienceSoft', address='No address', home='No home', mobile='No',
                                       work='No work', fax='No fax', email='No email1', email2='No email2',
                                       email3='No email3', homepage='No homepage', bday='1', bmonth='September',
                                       byear='1941', aday='9', amonth='May', ayear='1945', address2='TestAddress',
                                       phone2='Test phone2', notes='test note'))
    elif len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name='test name', header='test header', footer='test footer'))
    elif len(db.get_group_list_with_contacts()) == 0:
        random_contact = random.choice(db.get_contact_list())
        random_group = random.choice(db.get_group_list())
        app.contact.select_contact_by_id(random_contact.id)
        app.contact.add_to_group_by_group_id(random_group.id)

    rand_group_list_with_contacts = db.get_group_list_with_contacts()
    rand_gr = random.choice(rand_group_list_with_contacts)
    contacts_in_group_old = db.get_contact_list_in_group_and_homepage(rand_gr)
    rand_contact = random.choice(contacts_in_group_old)
    app.contact.select_group_to_view_by_group_id(rand_gr)
    app.contact.delete_contact_from_group_by_id(rand_contact)
    contacts_in_group_new = db.get_contact_list_in_group_and_homepage(rand_gr)
    assert len(contacts_in_group_old) - 1 == len(contacts_in_group_new)
    contacts_in_group_old.remove(rand_contact)
    assert contacts_in_group_old == contacts_in_group_new
    if check_ui:
        assert sorted(contacts_in_group_new, key=Contact.id_or_max) == sorted(app.contact.count_in_group(rand_gr), key=Contact.id_or_max)
