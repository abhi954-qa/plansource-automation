from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def open_login_page(self, url):
        self.driver.get(url)
        self.logger.info("Opened login URL.")

    def login(self, username, password):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "user_name"))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(password)
        self.driver.find_element(By.ID, "logon_submit").click()
        self.logger.info("Submitted login form.")

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Dashboard')]"))
            )
            self.logger.info("Login successful.")
            return True
        except:
            self.logger.error("Login failed.")
            return False
