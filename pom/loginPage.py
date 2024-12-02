class Login:
    def submit_login_form(self, user):
        self.username_field.fill(user["username"])
        self.password_field.fill(user["password"])
        self.submit_button.click()
    def navigate(self):
        self.page.goto("https://console-integ.reach5.co/")