# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    return "+" + "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 31))


def random_month():
    return random.choice(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                           'October', 'November', 'December'])


def random_year():
    return str(random.randrange(2000))


def random_email(maxlen):
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@"\
           + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + ".com"


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
            photo='E:\\1332955017586.jpg', title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home=random_phone(10), mobile=random_phone(10),
            work=random_phone(10), fax=random_phone(10), email=random_email(10), email2=random_email(10),
            email3=random_email(10), homepage=random_string("home", 10), bday=random_day(), bmonth=random_month(),
            byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
            address2=random_string("address2", 10), phone2=random_phone(10), notes=random_string("note", 10))
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contacts_list()
    app.contact.press_add_new_contact()
    app.contact.fill_contact_info(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contacts_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
