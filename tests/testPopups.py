from pages.Popups import Popups
from playwright.sync_api import sync_playwright
import pytest
def test_popups():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        popups = Popups(page)
        popups.navigate()
        popups.verify_popups_page()
        popups.verify_alert_popup()
        page.reload()
        popups.verify_confirm_popup_OK()
        page.reload()   
        popups.verify_confirm_popup_Cancel()
        page.reload()    
        popups.verify_prompt_popup()
        page.reload()

