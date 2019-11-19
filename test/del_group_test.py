from model.group import Group


def test_del_group_testcase(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    old_groups = app.group.get_groups_list()
    app.group.delete_first_group()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups[0:1] = []
    assert old_groups == new_groups

