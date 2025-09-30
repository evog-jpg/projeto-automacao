from pages.slider_page import SliderPage

def test_slider_interaction(driver):
    slider_page = SliderPage(driver)
    slider_page.navigate()
    slider_page.set_slider_value_keys(100)
    assert slider_page.get_slider_value() == "100"