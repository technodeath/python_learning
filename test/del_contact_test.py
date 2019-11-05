def test_del_contact_testcase(app):
    app.session.login(username='admin', password='secret')
    app.contact.delete_first_contact()
    app.session.logout()