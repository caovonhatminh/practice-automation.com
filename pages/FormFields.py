from tkinter import dialog
from playwright.sync_api import Page,expect
from requests import options
import time
class FormFields:
    def __init__(self, page: Page):
        self.page = page
        self.form_fields_button = page.locator("//a[text()='Form Fields']")
        self.name_input = page.locator("#name-input")
        self.password_input = page.locator("//input[@type='password']")
        self.water_checkbox = page.locator("//input[@id='drink1']")
        self.milk_checkbox = page.locator("//input[@id='drink2']")
        self.coffee_checkbox = page.locator("//input[@id='drink3']")
        self.wine_checkbox = page.locator("//input[@id='drink4']")
        self.ctrl_alt_delight_checkbox = page.locator("//input[@id='drink5']")
        self.red_radio = page.locator("//input[@id='color1']")
        self.blue_radio = page.locator("//input[@id='color2']")
        self.yellow_radio = page.locator("//input[@id='color3']")
        self.green_radio = page.locator("//input[@id='color4']")
        self.dropdown = page.locator("//select[@id='automation']")
        self.options = page.locator("//select[@id='automation']/option")
        self.email_input = page.locator("//input[@id='email']")
        self.message_textarea = page.locator("//textarea[@id='message']")
        self.submit_button = page.locator("//button[@class='custom_btn btn_hover']")


    def navigate(self):
        self.page.goto("https://practice-automation.com/")
    def veirfy_form_fields_page(self):
        self.form_fields_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/form-fields/")
    def fill_name_and_password(self, name: str, password: str):
        expect(self.name_input).to_be_visible()
        self.name_input.fill(name)
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        time.sleep(5)
    def check_favorite_drink_checkbox(self):
        self.water_checkbox.check()
        expect(self.water_checkbox).to_be_checked()
        self.milk_checkbox.check()
        expect(self.milk_checkbox).to_be_checked()
        self.coffee_checkbox.check()
        expect(self.coffee_checkbox).to_be_checked()
        self.wine_checkbox.check()
        expect(self.wine_checkbox).to_be_checked()
        self.ctrl_alt_delight_checkbox.check()
        expect(self.ctrl_alt_delight_checkbox).to_be_checked()
    def check_favorite_color_radio(self):
        self.red_radio.click()
        expect(self.red_radio).to_be_checked()
        self.blue_radio.click()
        expect(self.blue_radio).to_be_checked()
        self.yellow_radio.click()
        expect(self.yellow_radio).to_be_checked()
        self.green_radio.click()
        expect(self.green_radio).to_be_checked()
    def verify_dropdown_automation(self):
        expect(self.dropdown).to_be_visible()
        self.dropdown.click()
        expect(self.options).to_have_count(4)
        expect(self.options.nth(1)).to_have_text("Yes")
        expect(self.options.nth(2)).to_have_text("No")
        expect(self.options.nth(3)).to_have_text("Undecided")
        self.dropdown.select_option("yes")
        expect(self.dropdown).to_have_value("yes")
        time.sleep(5)
    def verify_email_input(self, email: str):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)
        time.sleep(5)
    def verify_message_textarea(self, message: str):
        expect(self.message_textarea).to_be_visible()
        self.message_textarea.fill(message)
        expect(self.message_textarea).to_have_value(message)
        time.sleep(5)
    def verify_submit_button(self):
        expect(self.submit_button).to_be_visible()
        self.submit_button.click()
    def verify_popup_message(self):
        with self.page.expect_dialog() as dialog_info:
            self.submit_button.click()
            dialog = dialog_info.value
            assert dialog.message == "Message received!"
            dialog.accept()
        
