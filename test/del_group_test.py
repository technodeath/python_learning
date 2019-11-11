from model.group import Group


def test_del_group_testcase(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    app.group.delete_first_group()
