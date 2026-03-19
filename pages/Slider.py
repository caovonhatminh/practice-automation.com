from playwright.sync_api import Page,expect
class Slider:
    def __init__(self, page: Page):
        self.page = page
        self.slider_button = page.locator("//a[text()='Sliders']")
        self.slider_bar = page.locator("//input[@id='slideMe']")

    def navigate(self):
        self.page.goto("https://practice-automation.com/")
    def verify_slider_page(self):
        self.slider_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/slider/")
    def verify_slider_functionality(self):
        expect(self.slider_bar).to_be_visible()
        self.slider_bar.fill("75")
        expect(self.slider_bar).to_have_value("75")  