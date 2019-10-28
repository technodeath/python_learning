# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username='admin', password='secret')
    app.press_add_new_contact()
    app.fill_contact_info(Contact(firstname='Aliaksandr', middlename='Igorevich', lastname='Kuzmitski',
                                       nickname='technodeath', photo='E:\\1332955017586.jpg', title='QA',
                                       company='ScienceSoft', address='No address', home='No home', mobile='No',
                                       work='No work', fax='No fax', email='No email1', email2='No email2',
                                       email3='No email3', homepage='No homepage', bday='1', bmonth='September',
                                       byear='1941', aday='9', amonth='May', ayear='1945', address2='TestAddress',
                                       phone2='Test phone2', notes='test note'))
    app.logout()