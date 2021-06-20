# -*- coding: utf-8 -*-
import random
import time

from model.project import Project


def test_delete_some_project(app):
    if len(app.soap.get_all_admin_projects()) == 0:
        app.project.create(Project(name="test" + str(round(time.time() * 1000))))

    old_projects = app.soap.get_all_admin_projects()
    index = random.randrange(len(old_projects))
    app.project.delete_by_index(index)
    new_projects = app.soap.get_all_admin_projects()

    assert len(old_projects) - 1 == len(new_projects)
    old_projects[index:index + 1] = []
    assert old_projects == new_projects

    assert sorted(new_projects, key=Project.id_or_max) == sorted(app.soap.get_all_admin_projects(), key=Project.id_or_max)