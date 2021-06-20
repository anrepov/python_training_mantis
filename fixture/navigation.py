class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("my_view_page.php"):
            wd.find_element_by_link_text("My View").click()

    def open_start_page(self):
        wd = self.app.wd
        wd.get(self.app.base_url)

    def accept_alert(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()
