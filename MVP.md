## Minimum Viable Product

### Building an Airbnb Pricing Tool for NYC Properties

The goal of this project is to create an Airbnb price prediction tool based on features of a property that hosts can use to set a price that is appropriate and
optimal for profitability yet affordable to guests.

To start exploring this goal, I selected the numeric features I believe may be strong predictors of price. These numeric features of interest are:
no. bedrooms, overall rating, no. listing reviews, location rating, cleanliness rating, no. host ratings, host response rate, and months since host joined

I created a pairplot of these numeric features of interest to observe the feature-to-feature relations and feature distributions.
![pairplot_airbnb](https://user-images.githubusercontent.com/87044440/128139361-9b35a615-7cdb-4768-b341-43f17cb4a88c.jpg)

One takeaway is that the target, price per night, as well as other features, may require log transformation to create a more even distribution. 
Additionally, while none of the relations are clearly linear, it appears that some expected patterns are visible. For example, higher overall ratings,
location ratings, and host response rates are related to higher listing prices.

I also created a heatmap of the feature correlations.
![Screen Shot 2021-08-04 at 3 39 54 AM](https://user-images.githubusercontent.com/87044440/128141481-5d957b9a-96fc-4dc0-9667-0ad65ff4e089.png)

One important takeaway is that cleanliness ratings are highly correlated with overall ratings, which makes logical sense. This may be a candidate for a feature
to be dropped.


I anticipate that one of the best predictors of price will be which borough of NYC a property is located in (i.e. Manhattan vs. Staten Island), and that other 
categorical features may show strong relations to price once incorporated as dummy variables. These additional features include superhost status, property type 
(i.e. condo, apartment, etc.), and facilities (i.e. air conditioning, heating, kitchen).
