from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group name"))
    app.group.modify_first_group(Group(name="New group edited name"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    app.group.modify_first_group(Group(header="New group edited header"))