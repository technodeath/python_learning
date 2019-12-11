# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_add_random_contact_to_random_group(app, db, json_contacts, json_groups, check_ui):
    if len(db.get_contact_list()) == 0:
        contact = json_contacts
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(contact)
    elif len(db.get_group_list()) == 0:
        group = json_groups
        app.group.create()
        app.group.fill_and_submit_new_group(group)

    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    contacts_in_group_old = db.get_contact_list_in_group(group.id)
    app.contact.select_contact_by_id(contact.id)
    app.contact.add_to_group_by_group_id(group.id)
    contacts_in_group_new = db.get_contact_list_in_group(group.id)
    assert len(contacts_in_group_old) + 1 == len(contacts_in_group_new)
    contacts_in_group_old.append(contact)
    if check_ui:
        assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(contacts_in_group_new, key=Contact.id_or_max)
