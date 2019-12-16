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
    elif db.get_all_contacts_id_list_in_contacts() == db.get_all_contacts_id_list_in_groups():
        contact = json_contacts
        group = random.choice(db.get_group_list())
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(contact)
        app.contact.select_contact_by_id(contact.id)
        app.contact.add_to_group_by_group_id(group.id)
    elif app.contact.diff(db.get_all_contacts_id_list_in_contacts(), db.get_all_contacts_id_list_in_groups()):
        for i in app.contact.diff(db.get_all_contacts_id_list_in_contacts(), db.get_all_contacts_id_list_in_groups()):
            group = random.choice(db.get_group_list())
            app.contact.select_contact_by_id(i)
            app.contact.add_to_group_by_group_id(group.id)

    contact = random.choice(db.get_contact_list())
    group = random.choice(db.get_group_list())
    contacts_in_group_old = db.get_info_about_contacts_from_group(group.id)
    app.contact.select_contact_by_id(contact.id)
    app.contact.add_to_group_by_group_id(group.id)
    contacts_in_group_new = db.get_info_about_contacts_from_group(group.id)
    assert len(contacts_in_group_old) + 1 == len(contacts_in_group_new)
    contacts_in_group_old.append(contact)
    assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(contacts_in_group_new, key=Contact.id_or_max)
    if check_ui:
        assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_vs_db(group.id), key=Contact.id_or_max)
