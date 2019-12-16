import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             db=name, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated ='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_info_about_contacts_from_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            query = """SELECT addressbook.id, addressbook.firstname, addressbook.lastname
                    FROM addressbook
                    INNER JOIN address_in_groups ON address_in_groups.id = addressbook.id WHERE address_in_groups.group_id = %s"""
            cursor.execute(query, group_id)
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_list_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            query = "select id from address_in_groups where deprecated ='0000-00-00 00:00:00' and group_id = %s"
            cursor.execute(query, group_id)
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list

    def get_all_contacts_id_list_in_groups(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where deprecated ='0000-00-00 00:00:00' order by id ASC")
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list

    def get_all_contacts_id_list_in_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from addressbook where deprecated ='0000-00-00 00:00:00' order by id ASC")
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list

    def get_contact_list_in_group_and_homepage(self, group_id):  # bug, deleted contact doesn't remove from address_in_groups
        list = []
        cursor = self.connection.cursor()
        try:
            query = """SELECT address_in_groups.id, address_in_groups.group_id, addressbook.id
                    FROM address_in_groups
                    INNER JOIN addressbook ON address_in_groups.id = addressbook.id WHERE address_in_groups.group_id = %s"""
            cursor.execute(query, group_id)
            for row in cursor:
                list.append(row[0])
        finally:
            cursor.close()
        return list

    def get_group_list_with_contacts(self):
        list = []
        cursor = self.connection.cursor()
        try:
            query = """SELECT address_in_groups.id, address_in_groups.group_id, addressbook.id
                    FROM address_in_groups
                    INNER JOIN addressbook ON address_in_groups.id = addressbook.id"""
            cursor.execute(query)
            for row in cursor:
                list.append(row[1])
        finally:
            cursor.close()
        return list

    def get_contacts_info_from_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            query = """SELECT id, lastname, firstname, address, email, email2, email3,
             work, phone2, home, mobile from addressbook where deprecated ='0000-00-00 00:00:00'"""
            cursor.execute(query)
            for row in cursor:
                (id, lastname, firstname, address, email, email2, email3, work, phone2, home, mobile) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                    email=email, email2=email2, email3=email3, work=work, phone2=phone2,
                                    home=home, mobile=mobile))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_phones_info_from_db(self):
        list = []
        cursor = self.connection.cursor()
        try:
            query = "SELECT id, work, phone2, home, mobile from addressbook where deprecated ='0000-00-00 00:00:00'"
            cursor.execute(query)
            for row in cursor:
                (id, work, phone2, home, mobile) = row
                list.append(Contact(id=str(id), work=work, phone2=phone2, home=home, mobile=mobile))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
