In this assignment, we analyzed and visualized New York City yellow taxi trip data for January 2023. The data was collected from the following webpage, which is a data record for the Taxi and Limousine Commission(TLC):
https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

We performed exploratory data analysis (EDA) on the dataset and cleaned the data by removing rows with missing values. We then filtered the data to include trips with a fare amount of at least $10 and a trip distance of at least 1 mile.

To gain insights from the dataset, we calculated the average fare amount per passenger count and the total fare amount per pickup hour of the day. We also computed the mean and median values for trip distance and fare amount.

We then visualized the data by creating histograms, scatter plots, and line charts to display trip distances, fare amounts, and total fare amounts per pickup hour. These visualizations helped us better understand the trends and patterns in the data.

To enhance our analysis, we merged the taxi trip data with a Taxi Zone Lookup Table dataset to obtain borough information for each pickup and drop-off location. After aggregating the number of pickups and drop-offs per borough, we created heatmaps to visualize the spatial distribution of taxi trips across New York City boroughs.

Throughout this assignment, we leveraged various Python libraries, including Polars, Pandas, Matplotlib, and Geopandas, to process, analyze, and visualize the data. The insights and visualizations we generated could help stakeholders make informed decisions regarding taxi services, demand patterns, and fare policies in New York City.
