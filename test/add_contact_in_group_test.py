# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
from data.contacts import testdata_contacts
from data.groups import testdata_groups
import random


def test_add_random_contact_to_random_group(app, db, check_ui, orm):
    if len(db.get_contact_list()) == 0:
        contact = testdata_contacts
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(contact)
    if len(db.get_group_list()) == 0:
        group = testdata_groups
        app.group.create()
        app.group.fill_and_submit_new_group(group)
    if len(orm.get_contacts_not_in_group(Group(id=random.choice(db.get_group_list()).id))) == 0:
        contact = testdata_contacts
        app.contact.press_add_new_contact()
        app.contact.fill_contact_info(contact)

    rand_group = random.choice(db.get_group_list())
    contacts_not_in_groups = orm.get_contacts_not_in_group(Group(id=rand_group.id))
    contact = random.choice(contacts_not_in_groups)
    contacts_in_group_old = db.get_info_about_contacts_from_group(rand_group.id)
    app.contact.select_contact_by_id(contact.id)
    app.contact.add_to_group_by_group_id(rand_group.id)
    contacts_in_group_new = db.get_info_about_contacts_from_group(rand_group.id)
    assert len(contacts_in_group_old) + 1 == len(contacts_in_group_new)
    contacts_in_group_old.append(contact)
    assert sorted(contacts_in_group_old) == sorted(contacts_in_group_new)

    if check_ui:
        assert sorted(contacts_in_group_old, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list_vs_db(rand_group.id), key=Contact.id_or_max)
