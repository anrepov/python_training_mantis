# -*- coding: utf-8 -*-
import time

from model.project import Project


def test_add_project(app):
    project = Project(name="test" + str(round(time.time() * 1000)), description="descr")

    old_projects = app.soap.get_all_admin_projects()
    app.project.create(project)
    new_projects = app.soap.get_all_admin_projects()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
