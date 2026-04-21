from pages.Calendars import Calendars
from playwright.sync_api import sync_playwright


def test_calendars():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        calendars = Calendars(page)

        calendars.navigate()
        calendars.verify_calendars_page()
        selected_date = calendars.verify_select_date()
        calendars.verify_submit_button()
        calendars.verify_submit_successfully(selected_date)

        browser.close()
