from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SelectPlansPage:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.wait = WebDriverWait(driver, 10)

    NEXT_SHOP_BENEFITS_BTN = (By.XPATH, "//span[text()= 'Next: Shop for Benefits']")
    UPDATE_CART_BTN = (By.XPATH, "//div[text()='Update Cart']")

    def click_next_shop_benefits(self):
        self.logger.info("Clicking on Next Shop Benefits button..")
        self.wait.until(EC.element_to_be_clickable(self.NEXT_SHOP_BENEFITS_BTN)).click()


    def shop_plan(self):
        """
        plan_type: 'Medical' or 'Voluntary Employee'
        """

        shop_button = self.driver.find_element(
            By.XPATH, "//a[@href='/subscriber/benefit/121136132']"
        )
        self.logger.info("Clicking on Shop button..")
        shop_button.click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Select your Medical Plan']")))

        # Click "Update Cart"
        self.logger.info("Clicking on Update Cart button..")
        update_btn = self.driver.find_element(*self.UPDATE_CART_BTN)
        update_btn.click()
