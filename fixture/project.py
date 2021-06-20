from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def fill_project_data(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_project_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]//a")[index].click()

    def create(self, project):
        wd = self.app.wd
        self.app.navigation.open_manage_projects_page()
        wd.find_element_by_xpath("//input[@value = 'Create New Project']").click()
        self.fill_project_data(project)
        wd.find_element_by_xpath("//input[@value = 'Add Project']").click()
        self.app.navigation.open_manage_projects_page()
        self.project_cache = None

    def modify_by_index(self, project, index):
        wd = self.app.wd
        self.app.navigation.open_manage_projects_page()
        self.select_project_by_index(index)
        self.fill_project_data(project)
        wd.find_element_by_xpath("//input[@value = 'Update Project']").click()
        self.app.navigation.open_manage_projects_page()
        self.project_cache = None

    def delete_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_manage_projects_page()
        self.select_project_by_index(index)
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        wd.find_element_by_xpath("//input[@value = 'Delete Project']").click()
        self.app.navigation.open_manage_projects_page()
        self.project_cache = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_manage_projects_page()
        return len(wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]"))

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.app.navigation.open_manage_projects_page()
            self.project_cache = []

            for row in wd.find_elements_by_xpath(
                    "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]/."):
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].find_element_by_tag_name("a").text
                id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)
