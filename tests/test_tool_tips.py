from pages.tool_tips_page import ToolTipsPage
from selenium.webdriver.common.by import By
import pytest
from utils.data_loader import load_json_data

test_data = load_json_data("data/test_data.json")

@pytest.mark.widgets
def test_button_tooltip(driver):
    """Tests the tooltip on the button."""
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

@pytest.mark.widgets
def test_tooltips_hover_input(driver):
    tool_tips_page = ToolTipsPage(driver)
    tool_tips_page.navigate(test_data["tool_tips_url"])

    # Hover over input field and check tooltip
    tool_tips_page.hover_over_input_field()

    field_tooltip_text = tool_tips_page.get_input_field_tooltip_text()
    assert field_tooltip_text == test_data["tool_tip_field_text"]
