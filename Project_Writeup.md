# Predicting the Prices of Airbnb Stays in New York City
Varsha Garla


## Abstract
This goal of this project was to use regression models to predict the price of an Airbnb listing in New York City given a number of a features. Airbnb hosts face the difficult decision of determining how much money to charge for their rental property. If the price is too high, customers may seek alternatives; meanwhile, if the price is too low, they could lose potential income. Thus, I sought to refine a model for hosts that will recommend an appropriate price for their listing that is optimal for the host's profitability yet affordable to guests.

## Design
This project consisted of several phases, [1] webscraping data on Airbnb listings in New York City, [2] cleaning and processing the data, and [3] iterating over different regression models incorporating Airbnb listing features in order to predict price. I began with a wide array of numerical and categorical features available on [Airbnb's website](https://www.airbnb.com/) and explored their predictive values in order to build a model with high predictive performance and interpretability so that hosts can assess the values of their properties and obtain reasonable price recommendations.

## Data
Information was scraped for five queries: stays in each of the five boroughs of New York City (Manhattan, Brooklyn, the Bronx, Staten Island, and Queens). Five thousand listings were scraped per borough yielding a raw data set of 25,000 rows. Due to a high volume of duplicate search results and missing values, the final data set contained ~950 rows. Categorical and numerical features were extracted and processed from the raw data. Examples of features include the property type from the header, the number of bedrooms, and the location rating. The target feature was the price per night.

## Algorithms
_Feature Engineering_
- Converting categorical features such as borough and property type to dummy variables
- One-Hot-Encoding for singular features such as superhost status
- Adding deviation feature for occupancy relative to borough

_Models_

Simple linear regression and RidgeCV regression were used before settling on LassoCV forest as the model with strongest cross-validation performance. 

_Model Evaluation and Selection_

The entire training dataset was split into 80/20 train vs. holdout, and all scores reported below were calculated with 5-fold cross validation on the training portion only. Predictions on the 20% holdout were limited to the very end, so this split was only used and scores seen just once. Cross-validated R^2 scores were the main metric for comparing and tuning models.

**Final Model**
- alpha: 0.307
- Holdout R^2 score: 0.561
- Mean absolute error (MAE): 38.47
- Feature coefficients:

![Screen Shot 2021-08-06 at 12 26 45 AM](https://user-images.githubusercontent.com/87044440/128456152-d5370e22-7dea-457f-b976-da5a9ae440de.png)


## Tools
- BeautifulSoup and Selenium for webscraping
- Numpy and Pandas for data manipulation
- Scikit-learn for modeling
- Matplotlib and Seaborn for visualization

## Communication
The presentation slide deck and visuals can be viewed in this repository.
