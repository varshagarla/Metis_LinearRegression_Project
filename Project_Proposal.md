## Linear Regression Project Proposal

### Question/need:
This project aims to predict the price of an Airbnb listing given a number of a features. Airbnb hosts face the difficult decision of determining how much
money to charge for their rental property. If the price is too high, customers may seek alternatives; meanwhile, if the price is too low, they could lose potential income. I seek to create a tool for hosts that will provide an appropriate price for their listing that is optimal for the host's profitability yet affordable to guests.

### Data Description:
I plan to scrape data directly from [Airbnb's website](https://www.airbnb.com/). An individual "row" or unit of analysis would be one listing that appears in
the search results for stays. As of now, I plan to set the following search parameters on Airbnb:
* Location: Poconos, Pennsylvania (popular region for outfoor activities year-round)
* Date: August 14-21, 2021
* Guests: 4 adults

_I may choose to look at New York City, NY instead if I want to analyze more than a 1,000 listings (i.e. 50,000)_

Examples of features I am interested in:
* cleaning_fee
* service_fee
* cnt_bedrooms
* cnt_beds
* cnt_baths
* rating_cleanliness
* rating_communication
* rating_location
* is_superhost
* facility_wifi
* facility_free_parking

### Tools:
- BeautifulSoup and Selenium for websraping the data
- statsmodels/sklearn for EDA and building the linear regression model
- seaborn for visiualization

### MVP Goal:
My MVP goal is to create a linear regression model that can predict the price of an Airbnb listing. I hope to apply my model using one listing's features and predict its price.

