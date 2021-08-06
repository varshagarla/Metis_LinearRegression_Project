from airbnb_scraper import Parser
import time

if __name__ == "__main__":

    locations = {
        'MANHATTAN': 'https://www.airbnb.com/s/Manhattan--New-York--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&query=Manhattan%2C%20New%20York%2C%20NY%2C%20United%20States&place_id=ChIJYeZuBI9YwokRjMDs_IEyCwo&adults=2&source=structured_search_input_header&search_type=autocomplete_click',
        'BRONX': 'https://www.airbnb.com/s/Bronx--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&adults=2&source=structured_search_input_header&search_type=autocomplete_click&query=Bronx%2C%20NY%2C%20United%20States&place_id=ChIJsXxpOlWLwokRd1zxj6dDblU',
        'BROOKLYN': 'https://www.airbnb.com/s/Brooklyn--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&adults=2&source=structured_search_input_header&search_type=autocomplete_click&query=Brooklyn%2C%20NY%2C%20United%20States&place_id=ChIJCSF8lBZEwokRhngABHRcdoI',
        'STATEN_ISLAND': 'https://www.airbnb.com/s/Staten-Island--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&adults=2&source=structured_search_input_header&search_type=autocomplete_click&query=Staten%20Island%2C%20NY%2C%20United%20States&place_id=ChIJ59T0ee9FwokReLy6NIUfJ1A',
        'QUEENS': 'https://www.airbnb.com/s/Queens--NY--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=october&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=flexible_dates&adults=2&source=structured_search_input_header&search_type=autocomplete_click&query=Queens%2C%20NY%2C%20United%20States&place_id=ChIJK1kKR2lDwokRBXtcbIvRCUE'
    }

    for location in locations:
        new_parser = Parser(locations[location], f'./{location}.csv')
        t0 = time.time()
        new_parser.parse()
        print(location, time.time() - t0)
