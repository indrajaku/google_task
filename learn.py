import time

from playwright.sync_api import Playwright,sync_playwright


with sync_playwright()as p:
    browser = p.chromium.launch(headless=False,timeout=9000)
    page = browser.new_page()
#     # page.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://www.google.com")
    time.sleep(20)
#     page.fill("//input[@placeholder='Username']","Admin")
#     page.fill("//input[@placeholder='Password']","admin123")
#     page.click("//button[@type='submit']")
#     page.screenshot(path="sample_images/praveen.png", full_page=True)
#     # page.tracing.stop(path = "trace.zip")
#     print("a")
hotel_rating = page.inner_text("//span[@class='MW4etd']")
print(hotel_rating)