from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()):
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group name"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == app.group.count()
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create()
#         app.group.fill_and_submit_new_group(Group(header="New group header"))
#     old_groups = app.group.get_groups_list()
#     group = Group(header="New group header")
#     group.id = old_groups[0].id
#     app.group.modify_first_group(group)
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
