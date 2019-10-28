# -*- coding: utf-8 -*-
from model.group import Group
from fixture.application import Application
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group_testcase(app):
    app.session.login(username='admin', password='secret')
    app.group.create()
    app.group.fill_and_submit_new_group(Group(name='test name', header='test header', footer='test footer'))
    app.session.logout()


def test_add_empty_group_testcase(app):
    app.session.login(username='admin', password='secret')
    app.group.create()
    app.group.fill_and_submit_new_group(Group(name='', header='', footer=''))
    app.session.logout()
