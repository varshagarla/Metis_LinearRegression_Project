import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import json
import time

import os

import pandas as pd

from multiprocessing import Pool

NYC_LINK = 'https://www.airbnb.com/s/New-York-City--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=august&flexible_trip_dates%5B%5D=september&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=New%20York%20City%2C%20NY%2C%20United%20States&place_id=ChIJOwg_06VPwokRYv534QaPC8g&checkin=2021-08-07&checkout=2021-08-14&adults=4&source=structured_search_input_header&search_type=autocomplete_click'

RULES_SEARCH_PAGE = {
    'url': {'tag': 'a', 'get': 'href'},
    'name': {'tag': 'div', 'class': '_5kaapu'},
    'header': {'tag': 'div', 'class': '_1olmjjs6'},
    'rooms': {'tag': 'div', 'class': '_3c0zz1'},
    'facilities': {'tag': 'div', 'class': '_3c0zz1', 'order': 1},
    'rating_overall': {'tag': 'span', 'class': '_10fy1f8'},
    'num_listing_reviews': {'tag': 'span', 'class': '_a7a5sx'},
    'price_per_night': {'tag': 'span', 'class': '_155sga30'},
    'superhost': {'tag': 'div', 'class': '_1tyrh76'},
}

RULES_DETAIL_PAGE = {
    'location': {'tag': 'span', 'class': '_pbq7fmm'},

    'price_per_night': {'tag': 'span', 'class': '_me8w3a0'},

    'fee_occ_tax': {'tag': 'span', 'class': '_1k4xcdh', 'order': -2},
    'fee_service': {'tag': 'span', 'class': '_1k4xcdh', 'order': -3},
    'fee_cleaning': {'tag': 'span', 'class': '_1k4xcdh', 'order': -4},

    'rating_cleanliness': {'tag': 'span', 'class': '_4oybiu', 'order': -6},
    'rating_accuracy': {'tag': 'span', 'class': '_4oybiu', 'order': -5},
    'rating_communication': {'tag': 'span', 'class': '_4oybiu', 'order': -4},
    'rating_location': {'tag': 'span', 'class': '_4oybiu', 'order': -3},
    'rating_check_in': {'tag': 'span', 'class': '_4oybiu', 'order': -2},
    'rating_value': {'tag': 'span', 'class': '_4oybiu', 'order': -1},

    'host_joined': {'tag': 'div', 'class': 's9fngse dir dir-ltr'},

    'num_host_ratings': {'tag': 'span', 'class': 'l1dfad8f dir dir-ltr'},

    'host_languages': {'tag': 'li', 'class': 'f19phm7j dir dir-ltr'},
    'host_response_rate': {'tag': 'li', 'class': 'f19phm7j dir dir-ltr', 'order': -2},
    'host_response_time': {'tag': 'li', 'class': 'f19phm7j dir dir-ltr', 'order': -1},

    'house_rules': {'tag': 'div', 'class': 'c1lue5su dir dir-ltr', 'order': -1},

}


def extract_listings(page_url, attempts=10):
    """Extracts all listings from a given page"""

    listings_max = 0
    listings_out = [BeautifulSoup('', features='html.parser')]
    for idx in range(attempts):
        try:
            answer = requests.get(page_url, timeout=5)
            content = answer.content
            soup = BeautifulSoup(content, features='html.parser')
            listings = soup.findAll("div", {"class": "_gig1e7"})
        except:
            # if no response - return a list with an empty soup
            listings = [BeautifulSoup('', features='html.parser')]

        if len(listings) == 20:
            listings_out = listings
            break

        if len(listings) >= listings_max:
            listings_max = len(listings)
            listings_out = listings

    return listings_out


def extract_element_data(soup, params):
    """Extracts data from a specified HTML element"""
    # 1. Find the right tag
    if 'class' in params:
        elements_found = soup.find_all(params['tag'], params['class'])
    else:
        elements_found = soup.find_all(params['tag'])

    # 2. Extract the right element
    tag_order = params.get('order', 0)
    element = elements_found[tag_order]

    # 3. Get text
    if 'get' in params:
        output = element.get(params['get'])
    else:
        output = element.get_text()

    return output


def extract_listing_features(soup, rules):
    """Extracts all features from the listing"""
    features_dict = {}
    for feature in rules:
        try:
            features_dict[feature] = extract_element_data(soup, rules[feature])
        except:
            features_dict[feature] = 'empty'

    return features_dict


def extract_soup_js(listing_url, waiting_time=[20, 1]):
    """Extracts HTML from JS pages: open, wait, click, wait, extract"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--blink-settings=imagesEnabled=false')

    chromedriver_path = '/Applications/chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

    # if the URL is not valid - return an empty soup
    try:
        driver.get(listing_url)
    except:
        print(f"Wrong URL: {listing_url}")
        return BeautifulSoup('', features='html.parser')

    # waiting for an element on the bottom of the page to load ("More places to stay")
    try:
        myElem = WebDriverWait(driver, waiting_time[0]).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_4971jm')))
    except:
        pass

    # click cookie policy
    try:
        driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div[1]/section/footer/div[2]/button").click()
    except:
        pass
    # alternative click cookie policy
    try:
        element = driver.find_element_by_xpath("//*[@data-testid='main-cookies-banner-container']")
        element.find_element_by_xpath("//button[@data-testid='accept-btn']").click()
    except:
        pass

    # looking for amenities
    driver.execute_script("window.scrollTo(0, 0);")
    try:
        driver.find_element_by_class_name('_4r9yt52').click()
    except:
        pass  # amenities button not found

    time.sleep(waiting_time[1])

    detail_page = driver.page_source

    driver.quit()

    return BeautifulSoup(detail_page, features='html.parser')


def scrape_detail_page(base_features):
    """Scrapes the detail page and merges the result with basic features"""

    detailed_url = 'https://www.airbnb.com' + base_features['url']
    soup_detail = extract_soup_js(detailed_url)

    features_detailed = extract_listing_features(soup_detail, RULES_DETAIL_PAGE)
    features_amenities = extract_amenities(soup_detail)

    features_detailed['amenities'] = features_amenities
    features_all = {**base_features, **features_detailed}

    return features_all


def extract_amenities(soup):
    amenities = soup.find_all('div', {'class': '_1b2umrx'})

    amenities_dict = {}
    for amenity in amenities:
        header = amenity.find('h3', {'class': '_14i3z6h'}).get_text()
        values = amenity.find_all('div', {'class': '_gw4xx4'})
        values = [v.find(text=True) for v in values]

        amenities_dict['amenity_' + header] = values

    return json.dumps(amenities_dict)


class Parser:
    def __init__(self, link, out_file):
        self.link = link
        self.out_file = out_file

    def build_urls(self, listings_per_page=20, pages_per_location=25):
        """Builds links for all search pages for a given location"""
        url_list = []
        for i in range(pages_per_location):
            offset = listings_per_page * i
            url_pagination = self.link + f'&items_offset={offset}'
            url_list.append(url_pagination)
            self.url_list = url_list

    def process_search_pages(self):
        """Extract features from all search pages"""
        features_list = []
        for page in self.url_list:
            listings = extract_listings(page)
            for listing in listings:
                features = extract_listing_features(listing, RULES_SEARCH_PAGE)
                features['sp_url'] = page
                features_list.append(features)

        self.base_features_list = features_list

    def process_detail_pages(self):
        """Runs detail pages processing in parallel"""
        n_pools = os.cpu_count() // 2
        with Pool(n_pools) as pool:
            result = pool.map(scrape_detail_page, self.base_features_list)
        pool.close()
        pool.join()

        self.all_features_list = result

    def save(self, feature_set='all'):
        if feature_set == 'basic':
            pd.DataFrame(self.base_features_list).to_csv(self.out_file, index=False)
        elif feature_set == 'all':
            pd.DataFrame(self.all_features_list).to_csv(self.out_file, index=False)
        else:
            pass

    def parse(self):
        self.build_urls()
        self.process_search_pages()
        self.process_detail_pages()
        self.save('all')


if __name__ == "__main__":
    new_parser = Parser(NYC_LINK, './test.csv')
    t0 = time.time()
    new_parser.parse()
    print(time.time() - t0)
