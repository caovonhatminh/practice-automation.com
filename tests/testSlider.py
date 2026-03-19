from pages.Slider import Slider
from playwright.sync_api import sync_playwright
import time
def test_sliders():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False) # Đặt headless=True để chạy ngầm, hoặc False để xem trình duyệt
        page = browser.new_page()
        slider = Slider(page)
        slider.navigate()
        slider.verify_slider_page()
        slider.verify_slider_functionality()
        time.sleep(5)