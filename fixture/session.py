
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # login
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input:nth-child(7)").click()


    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Выйти").click()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Выйти")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        print(wd.find_element_by_xpath('//*[@id="top"]/form/b').text)
        return wd.find_element_by_xpath('//*[@id="top"]/form/b').text == "(" + username + ")"

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)