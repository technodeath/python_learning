# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_delete_random_contact_from_random_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        contact = random.choice(db.get_contact_list())
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(contact)
    elif len(db.get_group_list()) == 0:
        group = random.choice(db.get_group_list())
        app.group.create()
        app.group.fill_and_submit_new_group(group)
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
