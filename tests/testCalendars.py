from pages.Calendars import Calendars
from playwright.sync_api import sync_playwright
import time
def test_calendars():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        calendars = Calendars(page)
        calendars.navigate()
        calendars.verify_calendars_page()
        time.sleep(5)
        calendars.verify_select_date()
        time.sleep(5)
        calendars.verify_submit_button()
        time.sleep(5)
        calendars.verify_submit_successfully()
        time.sleep(5)