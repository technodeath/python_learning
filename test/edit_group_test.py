from model.group import Group


def test_edit_group_testcase(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group header"))
    app.group.edit_first_group()
    app.group.fill_and_submit_edit_group(Group(name='test name', header='test header', footer='test footer'))