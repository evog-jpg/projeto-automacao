from selenium.webdriver.common.by import By

class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/checkbox"

        self.expand_all_button = (By.CSS_SELECTOR, "button[title='Expand all']")
        self.notes_checkbox = (By.XPATH, "//label[@for='tree-node-notes']")

    def navigate(self):
        self.driver.get(self.url)

    def expand_all(self):
        self.driver.find_element(*self.expand_all_button).click()

    def check_box(self):
        self.driver.find_element(*self.notes_checkbox).click()

    def check_input(self):
        return self.driver.find_element(By.ID, "tree-node-notes").is_selected()

    def get_output_text(self):
        return self.driver.find_element(*self.notes_checkbox).is_selected()
