import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_double_click_with_screenshots(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(double_click_btn).perform()
    driver.save_screenshot("screenshots/1_after_double_click.png")
    double_click_message = driver.find_element(By.ID, "doubleClickMessage")
    assert "You have done a double click" in double_click_message.text

def test_right_click_with_screenshots(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    right_click_btn = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(right_click_btn).perform()
    driver.save_screenshot("screenshots/1_after_right_click.png")
    right_click_message = driver.find_element(By.ID, "rightClickMessage")
    assert "You have done a right click" in right_click_message.text

def test_dynamic_click_with_screenshots(driver):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)

    dynamic_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    dynamic_click_btn.click()
    driver.save_screenshot("screenshots/1_after_dynamic_click.png")
    dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage")
    assert "You have done a dynamic click" in dynamic_click_message.text