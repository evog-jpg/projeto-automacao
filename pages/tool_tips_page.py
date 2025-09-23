from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

class ToolTipsPage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.wait = WebDriverWait(driver, 10)
        self.button_tooltip = (By.ID, "toolTipButton")
        self.input_field_tooltip = (By.ID, "toolTipTextField")

    def navigate(self, url):
        self.driver.get(url)

    def hover_over_button(self):
        self.actions.move_to_element(self.driver.find_element(*self.button_tooltip)).perform()

    def hover_over_input_field(self):
        self.actions.move_to_element(self.driver.find_element(*self.input_field_tooltip)).perform()

    def get_button_tooltip_text(self):
        self.wait.until(lambda d: d.find_element(By.CLASS_NAME, "tooltip-inner").is_displayed())
        tooltip = self.driver.find_element(By.CLASS_NAME, "tooltip-inner")
        return tooltip.text

    def get_input_field_tooltip_text(self):
        self.wait.until(lambda d: d.find_element(By.CLASS_NAME, "tooltip-inner").is_displayed())
        tooltip = self.driver.find_element(By.CLASS_NAME, "tooltip-inner")
        return tooltip.text

