from model.group import Group
from random import randrange


def test_del_some_group_testcase(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[index:index+1] = []
    assert old_groups == new_groups

