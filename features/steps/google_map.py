from behave import given,when, then
from playwright.sync_api import sync_playwright
import csv

def initialize_browser():
    """Open Desktop|FSE application or a specific URL
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, timeout=8000)
    pw_context = browser.new_context().new_page()
    return pw_context

@given("Indraja on google homepage search for google maps")
def google_search(context):
    context.page = initialize_browser()
    context.page.goto("https://www.google.com/maps/@21.0686228,82.7525294,5z")
    context.page.wait_for_load_state("networkidle")
    context.page.locator("//input[@aria-label='Search Google Maps']").click()
    context.page.locator("//input[@aria-label='Search Google Maps']").fill("hotels")


@when("she click on google maps link")
def search_hotels(context):
    context.page.locator("//input[@aria-label='Search Google Maps']").click()


@then("she search for hotels,extract the hotel and save the hotel names")
def search_hotel(context):
    context.page.locator("//input[@aria-label='Search Google Maps']").fill("hotels")
    hotel_name = context.page.query_selector_all("//div[@class='NrDZNb']")
    names = [name.text_context().strip() for name in hotel_name]


    with open('hotel_name.csv', 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Hotel Names'])
        writer.writerows([[name]] for name in names)


# hotel_details = hotel_details[:int(n)]

    #     hotel.locm



# @then("she  a csv file")
#def extract_hotel_data(context):


