from model.group import Group


def test_edit_group_testcase(app):
    app.group.edit_first_group()
    app.group.fill_and_submit_edit_group(Group(name='test name', header='test header', footer='test footer'))