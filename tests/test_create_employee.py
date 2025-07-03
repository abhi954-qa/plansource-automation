import pytest

from pages.benefits_page import BenefitsPage
from pages.employee_page import EmployeePage
from pages.enrollment_page import EnrollmentPage
from pages.login_page import LoginPage
from pages.selectplans_page import SelectPlansPage
from utils.logger import setup_logger
from  utils.generator import generate_random_ssn, get_hire_date

BASE_URL = "https://partner-dev-benefits.plansource.com"
USERNAME = "plansource_test_admin"
PASSWORD = "password123"

logger = setup_logger()

@pytest.mark.usefixtures("driver")
def test_create_employee(driver):
    # Step 1: Login first
    login_page = LoginPage(driver, logger)
    login_page.open_login_page(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_login_successful(), "Login failed."

    # Step 2: Create employee
    employee_page = EmployeePage(driver, logger)
    employee_page.click_add_new_employee()

    employee_data = {
        "first_name": "Abhi",
        "last_name": "Basava",
        "email": "abhi.basava@example.com",
        "ssn": generate_random_ssn(),
        "password": "Test@1234",
        "Address 1":"ABC Building",
        "city":"Bangalore",
        "State":"Alabama",
        "Zip":"99501",
        "Country":"United States",
        "Birthdate":"05/07/1994",
        "Gender":"Male",
        "Marital Status":"Single",
        "hire_date": get_hire_date(),
        "eligible_date": get_hire_date(),
        "Employment Level":"F",
        "Location":"SCA",
        "Current Salary":"5",
        "Benefit Salary":"10"
    }

    employee_page.fill_employee_form(employee_data)
    assert employee_page.is_employee_created_successfully(), "Employee creation failed."

    benefits_page = BenefitsPage(driver,logger)
    benefits_page.start_new_hire_enrollment()

    assert benefits_page.is_user_directed_to_enrollment_page(),"User not directed to enrollment page"

    dependent_page = EnrollmentPage(driver,logger)
    dependent_page.add_dependent()

    assert dependent_page.is_dependent_created(),"Dependent not added"

    selectplans_page = SelectPlansPage(driver,logger)

    selectplans_page.click_next_shop_benefits()
    selectplans_page.shop_plan()