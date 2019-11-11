# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_testcase(app):
    app.group.create()
    app.group.fill_and_submit_new_group(Group(name='test name', header='test header', footer='test footer'))


def test_add_empty_group_testcase(app):
    app.group.create()
    app.group.fill_and_submit_new_group(Group(name='', header='', footer=''))
