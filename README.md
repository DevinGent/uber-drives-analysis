# Uber Drives Analysis
In this project we will use python to clean and perform Exploratory Data Analysis (EDA) on a dataset containing information on Uber trips.  In `uber_analysis.py` we will clean and preprocess the data.  The result has been saved as `CleanedData.csv`.

## Content Overview
### `uber_analysis.py`
In this script we first read, clean, and preprocess the dataset `My-Uber-Drives-2016.csv`.  
As part of the cleaning process duplicate and empty rows are dropped, along with any row corresponding to a trip averaging over 80 MPH.
The result is saved as `CleanedData.csv`.
The dataframe obtained has the following features.

| Feature | Description |
| ----- | ----- |
| Start Date | The date and time (in datetime format) the trip began. |
| End Date | The date and time (in datetime format) the trip ended. |
| Category | Whether the trip was for business or personal reasons. |
| Start | The start location, as a string. |
| End | The end location, as a string. |
| Miles | The length of the trip, in miles rounded to one decimal place, as a float. |
| Purpose | The purpose of the trip-- Meeting, Moving, Airport/Travel, etc. |
| Trip Time | The duration of the trip, in minutes, rounded to an int. |
| avg MPH | The average MPH during the trip (trip length / trip time in hours) rounded to one decimal place as a float. |
| Weekday | The day of the week the trip started. |
| Month | The month of the year the trip started. |
| Window | The time window the trip started. |

The feature 'Window' has the following possible values, assuming a 24 hour clock.
| Window | Start Time |
| ----- | ----- |
| Morning | 6-10 |
| Midday | 10-14 |
| Afternoon | 14-18 |
| Evening | 18-22 |
| Night | 22-02 |
| Late | 2-6 |

We perform exploratory analysis using the preprocessed dataframe and a combination of `matplotlib` and `seaborn`. 
Some of the resulting graphs are saved in the folder `Visuals` for demonstration.  For example, the number of trips taken in each month is shown in the following figure.
![The number of trips per month.](Visuals\Trips-by-Month.png)

Investigating the uptick of trips in the month of December, we see a difference in the proportion of trips with purpose Errand/Supplies during the month of December.
![Example showing trip purpose.](Visuals\Trip-Purpose.png)


## Dataset
The dataset used in our analysis, `My-Uber-Drives-2016.csv`, can be freely obtained from Kaggle via the following link:
[https://www.kaggle.com/datasets/zusmani/uberdrives](https://www.kaggle.com/datasets/zusmani/uberdrives) under the DcBL license.
It contains information on one person's Uber trips during the year 2016.

## Dependencies
The following python libraries are used in this project.
* `pandas`
* `matplotlib`
* `seaborn`
