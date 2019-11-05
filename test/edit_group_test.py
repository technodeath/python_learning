from model.group import Group


def test_edit_group_testcase(app):
    app.session.login(username='admin', password='secret')
    app.group.edit_first_group()
    app.group.fill_and_submit_edit_group(Group(name='test name', header='test header', footer='test footer'))
    app.session.logout()