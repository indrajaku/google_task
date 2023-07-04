
import pandas as ps
from behave import given, when, then
from playwright.sync_api import sync_playwright, expect


hotel_data = {
    'Hotel name': [],
    'Rating': [],
    'reviews': []
}

def initialize_browser():
    """Open Desktop|FSE application or a specific URL
    """
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, timeout=8000)
    pw_context = browser.new_context().new_page()
    return pw_context


@given("Indraja opens google search and searchs for google maps")
def google_search(context):
    """Open Desktop|FSE application or a specific URL
    """
    context.page = initialize_browser()
    context.page.goto("https://www.google.com/")


@when("she clicks on the google maps link")
def google_maps_link(context):
    """Open given specific URL
    """
    context.page.locator("//textarea[@title='Search']").click(timeout=5000)
    context.page.locator("//textarea[@title='Search']").fill("google maps")
    context.page.press("//textarea[@title='Search']", "Enter")
    context.page.locator("(//h3['Google Maps'])[1]").click()
    context.page.wait_for_load_state('networkidle')
    context.page.wait_for_load_state('domcontentloaded')


@when("she searches for the hotels in {location}")
def search_hotel(context, location):
    """searching hotels for given location

    :param context: context object
    :type context: behave.runner.Context
    :param location: location for searching hotels
    :type location: str
    """
    context.page.wait_for_load_state('networkidle')
    context.page.wait_for_load_state('domcontentloaded')
    context.page.locator("//input[@aria-label='Search Google Maps']").fill("hotels near " + location)
    context.page.locator('#searchbox-searchbutton').click()
    context.page.expect_navigation(wait_until='networkidle')
    context.page.expect_navigation(wait_until='domcontentloaded')


@when("she retrieves the details of the {n} hotels")
def hotel_names(context, n):
    """ retrieving the hotels details
        :param context: context object
        :type context: behave.runner.Context
        :param n: number of  hotels
        :type n: int
        """
    n = int(n)
    expect(context.page.locator("(//a[@class='hfpxzc'])[1]")).to_be_visible(timeout=10000)
    hotel_name = context.page.query_selector_all("//div[@class='NrDZNb']")
    hotel_rating = context.page.query_selector_all("//span[@class='MW4etd']")
    hotel_reviews = context.page.query_selector_all("//span[@class='UY7F9']")

    n = min(len(hotel_name), len(hotel_rating), len(hotel_reviews), n)
    for i in range(n):
        hotel_names = hotel_name[i].get_property('textContent')
        ratings = hotel_rating[i].get_property('textContent')
        review = hotel_reviews[i].get_property('textContent')

        hotel_data['Hotel name'].append(hotel_names)
        hotel_data['Rating'].append(ratings)
        hotel_data['reviews'].append(review)


@then("she saves the hotel names")
def save_csv(context):
    """ saves the hotels data in csv file
            :param context: context object
            :type context: behave.runner.Context

            """
    df = ps.DataFrame(hotel_data)
    csv_file = 'hotelss.csv'
    df.to_csv(csv_file, index=False)

    context.csv_file = csv_file
    context.page.context.close()
