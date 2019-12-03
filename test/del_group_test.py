from model.group import Group
import random


def test_del_some_group_testcase(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_groups_list(), key=Group.id_or_max)

