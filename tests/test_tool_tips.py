from pages.tool_tips_page import ToolTipsPage
from selenium.webdriver.common.by import By
import pytest

@pytest.mark.widgets
def test_tooltips_hover_button(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    # Hover over button and check tooltip
    tool_tips_page.hover_over_button()

    tooltip_text = tool_tips_page.get_button_tooltip_text()
    assert tooltip_text == test_data["tool_tip_button_text"]

@pytest.mark.widgets
def test_tooltips_hover_input(driver, test_data):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    # Hover over input field and check tooltip
    tool_tips_page.hover_over_input_field()

    field_tooltip_text = tool_tips_page.get_button_tooltip_text()
    assert field_tooltip_text == test_data["tool_tip_field_text"]
