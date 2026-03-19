from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logo = page.locator("//img[@class='attachment-full size-full']")
        self.course_title = page.locator("(//span[@class='nav-menu-item-inside'])[1]")
        self.blog_title = page.locator("(//span[@class='nav-menu-item-inside'])[2]")
        self.welcome_message = page.locator("//h1[@class='wp-block-heading']")
        self.paragraph = page.locator("//p[@class='wp-block-paragraph']")
        self.JavaScriptDelays_image = page.locator("//img[@class='wp-image-12371 sp-no-webp']")
        self.JavaScriptDelays_title = page.locator("//a[text()='JavaScript Delays']")
        self.FormFields_image = page.locator("//img[@class='wp-image-12372 sp-no-webp']")
        self.FormFields_title = page.locator("//a[text()='Form Fields']")



    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def expect_element(self, selector: str):
        return expect(self.page.locator(selector))