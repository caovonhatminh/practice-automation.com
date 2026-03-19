from tkinter import dialog
from playwright.sync_api import Page,expect
from requests import options
import time
class Popups:
    def __init__(self, page: Page):
        self.page = page
        self.popups_button = page.locator("//a[text()='Popups']")
        self.alert_popup_button = page.locator("//button[@id='alert']")
        self.confirm_popup_button = page.locator("//button[@id='confirm']")
        self.prompt_popup_button = page.locator("//button[@id='prompt']")
    def navigate(self):
        self.page.goto("https://practice-automation.com/")
    def verify_popups_page(self):
        self.popups_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/popups/")
    def verify_alert_popup(self):
        self.page.reload()
        self.alert_popup_button.wait_for(state="visible")
        with self.page.expect_event("dialog") as dialog_info:
            self.alert_popup_button.click()
        dialog = dialog_info.value
        assert dialog.message == "Hi there, pal!"
        dialog.accept()
    def verify_confirm_popup_OK(self):
        self.page.reload()
        with self.page.expect_event("dialog") as dialog_info:
            self.confirm_popup_button.click()
        dialog = dialog_info.value
        assert dialog.message == "OK or Cancel, which will it be?"
        dialog.accept()
    def verify_confirm_popup_Cancel(self):
        with self.page.expect_event("dialog") as dialog_info:
            self.confirm_popup_button.click()
        dialog = dialog_info.value
        assert dialog.message == "OK or Cancel, which will it be?"
        dialog.dismiss()
    def verify_prompt_popup(self):
        with self.page.expect_event("dialog") as dialog_info:
            self.prompt_popup_button.click()
        dialog = dialog_info.value
        assert dialog.message == "Hi there, what's your name?"
        dialog.accept("Minh")
