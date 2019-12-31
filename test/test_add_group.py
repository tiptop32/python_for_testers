from model.group import Group
import pytest
from data.groups import testdata

def test_add_group(app, json_groups):
  group = json_groups
  old_groups = app.group.get_group_list()
  app.group.create(group)
  assert app.group.count() - len(old_groups) == 1
  new_groups = app.group.get_group_list()
  old_groups.append(group)
  assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

