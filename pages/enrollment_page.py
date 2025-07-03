import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EnrollmentPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)


    def add_dependent(self, first_name="Hiru", last_name="Basava", dob="05/07/2000", relationship="Child", gender="Male"):
        self.logger.info("Clicking on Get Started")
        time.sleep(6)
        get_started_btn =self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space(text())='Get Started']")))
        get_started_btn.click()

        self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Verify your Personal Information and make changes if needed']")))
        time.sleep(10)

        self.logger.info("Clicking on Next: Review My Family")
        next_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Next: Review My Family']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", next_btn)
        next_btn.click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='By adding a dependent']")))

        self.logger.info("Clicking on Add Family Member")
        self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,"a[href='/subscriber/family/new']"))).click()

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Please enter your Dependent Information']")))

        # Step 4: Fill form fields
        self.logger.info("Filling form fields")
        self.wait.until(EC.presence_of_element_located((By.ID, "first_name"))).send_keys(first_name)
        self.driver.find_element(By.ID, "last_name").send_keys(last_name)
        self.driver.find_element(By.ID, "birthdate").send_keys(dob)
        gender_btn = self.driver.find_element(By.XPATH, "//button[@data-id='gender']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", gender_btn)
        self.driver.execute_script("arguments[0].click();", gender_btn)
        time.sleep(0.3)
        male_option = self.driver.find_element(By.XPATH,"//span[text()= 'Male']")
        self.driver.execute_script("arguments[0].click();", male_option)

        relationship_btn = self.driver.find_element(By.CSS_SELECTOR, "button[data-id='relationship']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", relationship_btn)
        self.driver.execute_script("arguments[0].click();", relationship_btn)

        self.driver.find_element(By.XPATH, "//span[text()='Child']").click()

        self.logger.info("Clicking on Save")
        self.driver.find_element(By.XPATH, "//span[text()='Save']").click()


    def is_dependent_created(self, expected_text="Review the Dependent Information on file below"):
        try:
            self.logger.info("Waiting for text to appear...")
            elem = self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Review the Dependent Information on file below']")))
            actual_text = elem.text.strip()
            self.logger.info(f"Success message received: {actual_text}")
            return expected_text in actual_text
        except Exception as e:
            self.logger.error(f"Failed to verify success message: {e}")
            return False