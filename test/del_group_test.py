def test_del_group_testcase(app):
    app.session.login(username='admin', password='secret')
    app.group.delete_first_group()
    app.session.logout()