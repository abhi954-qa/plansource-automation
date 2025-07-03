from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BenefitsPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)
        self.SUCCESS_MSG= (By.XPATH, "//h2[text()='Shop and Enroll in Benefits']")

    def start_new_hire_enrollment(self):
        new_hire_button = (By.LINK_TEXT, "New Hire Enrollment")

        # Wait until clickable and then click
        self.wait.until(EC.element_to_be_clickable(new_hire_button)).click()

        # Wait for enrollment page load
        self.wait.until(EC.url_contains("/subscriber"))


    def is_user_directed_to_enrollment_page(self, expected_text="Shop and Enroll in Benefits"):
        try:
            self.logger.info("Waiting for text to appear...")
            elem = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MSG))
            actual_text = elem.text.strip()
            self.logger.info(f"Success message received: {actual_text}")
            return expected_text in actual_text
        except Exception as e:
            self.logger.error(f"Failed to verify success message: {e}")
            return False