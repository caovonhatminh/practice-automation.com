from pages.FormFields import FormFields
from playwright.sync_api import sync_playwright
import pytest

def test_form_fields():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        form_fields = FormFields(page)
        form_fields.navigate()
        form_fields.veirfy_form_fields_page()
        form_fields.fill_name_and_password("Minh", "123123")
        form_fields.check_favorite_drink_checkbox()
        form_fields.check_favorite_color_radio()
        form_fields.verify_dropdown_automation()
        form_fields.verify_email_input("minh@gmail.com")
        form_fields.verify_message_textarea("This is a test message.")
        form_fields.verify_submit_button()
        form_fields.verify_popup_message()