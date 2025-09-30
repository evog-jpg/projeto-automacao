from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class SliderPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/slider"
        self.slider = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/span/input')
        self.slider_value = (By.ID, "sliderValue")
        self.wait = WebDriverWait(driver, 10)

    def navigate(self):
        self.driver.get(self.url)

    def set_slider_value_keys(self, target_value, pause=0.01, max_steps=500):
        """Foca o slider e envia ARROW_RIGHT / ARROW_LEFT até o valor desejado. Mais lento, mas bem estável (não depende de offset em pixels)."""
        slider_element = self.driver.find_element(*self.slider)
        ActionChains(self.driver).move_to_element_with_offset(slider_element, 1, 0).click_and_hold().move_by_offset(5, 0).release().perform()
        current = int(slider_element.get_attribute("value"))
        target = int(target_value)
        steps = 0

        # decide direção
        key = Keys.ARROW_RIGHT if current < target else Keys.ARROW_LEFT

        while current != target and steps < max_steps:
            slider_element.send_keys(key)
            time.sleep(pause)  # dá tempo pro UI atualizar
            current = int(self.driver.find_element(*self.slider_value).get_attribute("value"))
            steps += 1

        if current != target:
            raise RuntimeError(f"Não foi possível atingir {target} via keys (chegou em {current})")

    def get_slider_value(self):
        return self.driver.find_element(*self.slider_value).get_attribute("value")
