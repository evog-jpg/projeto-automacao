from pages.text_box_page import TextBoxPage
from selenium.webdriver.common.by import By
import time

def test_fill_form_with_pom(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.navigate()

    # Test data
    full_name = "Eduardo"
    email = "evog@cesar.org.br"
    current_address = "rua barao de itamaracá, 409"
    permanent_address = "rua barao de itamaracá, 409"

    # Fill and submit form using page object methods
    text_box_page.fill_form(full_name, email, current_address, permanent_address)
    text_box_page.submit()

    output = text_box_page.get_output_text()

    assert full_name in output
    assert email in output
    assert current_address in output
    assert permanent_address in output