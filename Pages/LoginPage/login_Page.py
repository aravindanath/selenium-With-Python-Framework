import Utilities.custom_logger as cl
import logging
from Base.basepage import BasePage

class LoginPage(BasePage):

    log=cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_link = "Login"
    username_field = "user_email"
    password_field = "user_password"
    loginButton_link = "commit"

    # def getLoginField(self):
    #     return self.driver.find_element(By.LINK_TEXT, self.login_link)
    #
    # def getUserNameField(self):
    #     return self.driver.find_element(By.ID, self.username_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self.password_field)
    #
    # def getLoginButtonLink(self):
    #     return self.driver.find_element(By.NAME, self.loginButton_link)

    def clickLoginLink(self):
        self.elementClick(self.login_link, locatorType="link")

    def enteremail(self, email):
        self.sendKeys(email, self.username_field)

    def enterpassword(self, password):
        self.sendKeys(password, self.password_field)

    def clickLoginButton(self):
        self.elementClick(self.loginButton_link, locatorType="name")

    def login(self, email=" ", password=" "):
        self.clickLoginLink()
        self.driver.implicitly_wait(5)
        self.enteremail(email)
        self.enterpassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result=self.isElementPresent("gravatar", locatorType="class")
        return result

    def verifyLoginFailed(self):
        result=self.isElementPresent("//div[contains(text(),'Invalid email or password')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Google")
