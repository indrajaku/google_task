
from behave import given,when, then
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import re

def initialize_browser():
    """Open Desktop|FSE application or a specific URL
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, timeout=8000)
    pw_context = browser.new_context().new_page()
    return pw_context

@given("Indraja is on the google search page")
def google_search(context):
    """Open Desktop|FSE application or a specific URL
    """

    context.page = initialize_browser()

    context.page.goto("https://www.google.com")
    context.page.wait_for_load_state("networkidle")

@when('she searches for "{company}"')
def search_company(context,company):
    """Open Desktop|FSE application or a specific URL

    :param context: context - company
    :type context: behave.runner.Context
    :param host: context - company
    :type host: str
    """

    context.page.locator("//textarea[@title='Search']").click()
    context.page.locator("//textarea[@title='Search']").fill(company)
    context.page.press("//textarea[@title='Search']","Enter")

@when("she sees the company card")
def see_card(context):
    """Open Desktop|FSE application or a specific URL
    """

    try:
        context.page.wait_for_selector("//div[@class='SPZz6b']")
        assert context.page.query_selector("//div[@class='SPZz6b']")
        with context.page.expect_navigation():
            context.page.click("//img[@id='lu_map']")
    except PlaywrightTimeoutError:
        raise Exception("Company card has not appeared")


@then("she retrieves the latitude and logitude")
def retrieve_lat_log(context):
    """Open Desktop|FSE application or a specific URL

    """
    current_url = context.page.url
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)',current_url)
    latitude = match.group(1)
    longitude = match.group(2)
    context.latitude = latitude
    context.longitude = longitude
    context.page.close()

    print(f'Latitude:{latitude}')
    print(f'longitude:{longitude}')










