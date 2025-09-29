from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com"
        self.alerts_button = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[1]')
        self.alerts_page = (By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div[3]/div/ul/li[2]')
        self.see_alert_button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/button')
        self.button_after_5_seconds = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/button')
        self.confirm_box_button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/button')
        self.prompt_box_button = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[4]/div[2]/button')
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get(self.url)

    def click_alerts_windows_button(self):
        self.driver.find_element(*self.alerts_button).click()

    def goto_alerts_page(self):
        self.driver.find_element(*self.alerts_page).click()

    def click_see_alert_button(self):
        self.driver.find_element(*self.see_alert_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def click_button_after_5_seconds(self):
        self.driver.find_element(*self.button_after_5_seconds).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def click_confirm_box_button(self):
        self.driver.find_element(*self.confirm_box_button).click()
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def click_prompt_box_button(self):
         self.driver.find_element(*self.prompt_box_button).click()
         alert = self.wait.until(EC.alert_is_present())
         alert_text = alert.text
         alert.send_keys("Test User")
         alert.accept()
         return alert_text




