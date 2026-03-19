from playwright.sync_api import Page,expect
class Calendars:
    def __init__(self, page: Page):
        self.page = page
        self.calendars_button = page.locator("//a[text()='Calendars']")
        self.input_date = page.locator("//input[@id='g1065-1-selectorenteradate']")
        self.calendar_table = page.locator("//div[@class='dp-cal']")
        self.click_day_17 = page.locator("//button[text()='17']")
        self.submit_button = page.locator("(//button[@type='submit'])[1]")
        self.thankyou_text = page.locator("//h4[@id='contact-form-success-header-d789f525b512b8c992166cfbd9a18204964b4777']")
        self.date_17_successfully = page.locator("//div[@class='field-value']")

    def navigate(self):
        self.page.goto("https://practice-automation.com/")
    def verify_calendars_page(self):
        self.calendars_button.click()
        expect(self.page).to_have_url("https://practice-automation.com/calendars/")
    def verify_select_date(self):
        expect(self.input_date).to_be_visible()
        self.input_date.click()
        expect(self.calendar_table).to_be_visible()
        self.click_day_17.click()
        expect(self.input_date).to_have_value("2026-03-17")
    def verify_submit_button(self):
        expect(self.submit_button).to_be_visible()
        self.submit_button.click()
    def verify_submit_successfully(self):
        expect(self.thankyou_text).to_be_visible()
        expect(self.date_17_successfully).to_have_text("2026-03-17")
