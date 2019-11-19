from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create()
        app.group.fill_and_submit_new_group(Group(name="New group name"))
    old_groups = app.group.get_groups_list()
    group = Group(name="New group name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
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