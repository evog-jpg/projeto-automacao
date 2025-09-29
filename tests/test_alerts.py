from pages.alerts_page import AlertsPage
from selenium.webdriver.common.by import By

def test_alerts_interaction(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.navigate()
    alerts_page.click_alerts_windows_button()
    alerts_page.goto_alerts_page()
    assert alerts_page.click_see_alert_button() == "You clicked a button"

def test_alerts_5seconds(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.navigate()
    alerts_page.click_alerts_windows_button()
    alerts_page.goto_alerts_page()
    assert alerts_page.click_button_after_5_seconds() == "This alert appeared after 5 seconds"

def test_alerts_confirm_box(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.navigate()
    alerts_page.click_alerts_windows_button()
    alerts_page.goto_alerts_page()
    assert alerts_page.click_confirm_box_button() == "Do you confirm action?"

def test_alerts_prompt_box(driver):
    alerts_page = AlertsPage(driver)
    alerts_page.navigate()
    alerts_page.click_alerts_windows_button()
    alerts_page.goto_alerts_page()
    assert alerts_page.click_prompt_box_button() == "Please enter your name"