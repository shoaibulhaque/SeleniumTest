import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_form(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/")

        # Find existing fields and new fields
        name_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "name"))
        )
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "email"))
        )
        phone_number_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "phone_number"))  # Assuming name attribute
        )
        address_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "address"))  # Assuming name attribute
        )
        birth_date_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "birth_date"))  # Assuming name attribute
        )
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )

        # Fill in all fields with appropriate values
        name_field.send_keys("Alice")
        email_field.send_keys("alice@example.com")
        phone_number_field.send_keys("1234567890")  # Example phone number
        address_field.send_keys("123 Main St")  # Example address
        birth_date_field.send_keys("1990-01-01")  # Example birth date
        submit_button.click()

        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[text()='Data saved successfully!']"))
        )
        self.assertTrue(success_message.is_displayed())

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
