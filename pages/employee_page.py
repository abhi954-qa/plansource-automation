import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeePage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)
        self.SUCCESS_MESSAGE = (By.XPATH, "//span[contains(text(),'Basic Information')]")

    def click_add_new_employee(self):
        self.logger.info("Clicking on Add New Employee link.")
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add a New Employee"))).click()

    def fill_employee_form(self, employee_data):
        self.logger.info("Filling out employee creation form.")

        self.wait.until(EC.presence_of_element_located((By.ID, "first_name"))).send_keys(employee_data["first_name"])
        self.driver.find_element(By.ID, "last_name").send_keys(employee_data["last_name"])
        self.driver.find_element(By.ID, "ssn_text").send_keys(employee_data["ssn"])
        self.driver.find_element(By.ID, "address_1").send_keys(employee_data["Address 1"])
        self.driver.find_element(By.ID, "city").send_keys(employee_data["city"])
        self.driver.find_element(By.ID, "stateTypeahead").send_keys(employee_data["State"])
        self.driver.find_element(By.ID, "zip_code").send_keys(employee_data["Zip"])
        self.driver.find_element(By.ID, "countryTypeahead").send_keys(employee_data["Country"])
        self.driver.find_element(By.ID, "email").send_keys(employee_data["email"])
        self.driver.find_element(By.ID, "birthdate").send_keys(employee_data["Birthdate"])
        self.driver.find_element(By.ID, "gender").send_keys(employee_data["Gender"])
        self.driver.find_element(By.ID, "marital_status").send_keys(employee_data["Marital Status"])
        self.driver.find_element(By.ID, "password").send_keys(employee_data["password"])
        self.driver.find_element(By.ID, "hire_date").send_keys(employee_data["hire_date"])
        self.driver.find_element(By.ID, "benefits_start_date").send_keys(employee_data["eligible_date"])
        self.driver.find_element(By.ID, "employment_level").send_keys(employee_data["Employment Level"])
        self.driver.find_element(By.ID, "location").send_keys(employee_data["Location"])
        self.driver.find_element(By.ID, "current_salary").send_keys(employee_data["Current Salary"])
        self.driver.find_element(By.ID, "benefit_salary").send_keys(employee_data["Benefit Salary"])

        self.logger.info("Form filled. Submitting the form.")
        self.driver.find_element(By.ID, "btn_save").click()
        time.sleep(10)


    def is_employee_created_successfully(self, expected_text="Basic Information"):
        try:
            self.logger.info("Waiting for success message to appear...")
            elem = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
            actual_text = elem.text.strip()
            self.logger.info(f"Success message received: {actual_text}")
            return expected_text in actual_text
        except Exception as e:
            self.logger.error(f"Failed to verify success message: {e}")
            return False