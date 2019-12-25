# -*- coding: utf-8 -*-
from model.group import Group
import pytest


def test_add_group_testcase(app, db, json_groups, check_ui):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = db.get_group_list()
    with pytest.allure.step('When I add a group %s to the list' % group):
        app.group.create()
        app.group.fill_and_submit_new_group(group)
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        new_groups = db.get_group_list()
        old_groups.append(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)