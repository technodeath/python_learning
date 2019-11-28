# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group_testcase(app, json_groups):
    group = json_groups
    old_groups = app.group.get_groups_list()
    app.group.create()
    app.group.fill_and_submit_new_group(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)