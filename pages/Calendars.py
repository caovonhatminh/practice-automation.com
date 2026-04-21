from datetime import date
import re

from playwright.sync_api import Page,expect


class Calendars:
    def __init__(self, page: Page):
        self.page = page
        self.calendars_button = page.locator("//a[text()='Calendars']")
        self.input_date = page.locator("//input[@id='g1065-1-selectorenteradate']")
        self.submit_button = page.locator("form:has(#g1065-1-selectorenteradate) button[type='submit']").first
        self.thankyou_text = page.locator("h4", has_text="Thank you for your response.").first
        self.date_17_successfully = page.locator("//div[@class='field-value']").first

    def navigate(self):
        self.page.goto("https://practice-automation.com/")
    def verify_calendars_page(self):
        self.calendars_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/calendars/")
    def verify_select_date(self):
        expect(self.input_date).to_be_visible()
        selected_date = date.today().strftime("%Y-%m-%d")
        self.input_date.fill(selected_date)
        expect(self.input_date).to_have_value(selected_date)
        return selected_date
    def verify_submit_button(self):
        expect(self.submit_button).to_be_visible()
        self.submit_button.click()
    def verify_submit_successfully(self, expected_date: str):
        expect(self.page).to_have_url(re.compile(r"contact-form-sent="))
        expect(self.thankyou_text).to_be_visible()
        expect(self.date_17_successfully).to_have_text(expected_date)
