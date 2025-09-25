from pages.check_box_page import CheckBoxPage
from selenium.webdriver.common.by import By
import time

def test_check_box_commands(driver):
    check_box = CheckBoxPage(driver)
    check_box.navigate()

    check_box.expand_all()
    check_box.check_box()

    # Validate if checkbox was ticked
    assert check_box.check_input()
