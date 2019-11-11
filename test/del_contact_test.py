def test_del_contact_testcase(app):
    app.open_login_page()
    app.contact.delete_first_contact()