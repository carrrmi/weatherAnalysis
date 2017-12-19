## Weather Analysis

This repository contains data analysis based on a [weather-checking habits survey ran in 2015](https://github.com/fivethirtyeight/data/tree/master/weather-check)

The PowerPoint document is targetted to a general business audience. It is purposely simplified and non-technical. Its main goal is to communicate the meaning of the survey results in actionable terms.

The accompanying Excel file and [Tableau Viz](https://public.tableau.com/profile/carmen.chirita#!/vizhome/weather_check_survey/Story1) 
include the bulk of the analysis. Given the nature and the size of the datasets, these tools were more than sufficient for conveying the results. 

*Note: The rendering of the Tableau Public viz does not match exactly the rendering on the desktop version.*


#### Excel Analysis
The Excel spreadsheet has the following list of tabs:
* tab 1: weather-check_no_nulls - slightly massaged data and a few additional derived fields
* tab 2: Histograms-Data Sampling - data sample profiling (respondent distributions by age & region, age & income, etc)
* tab 3: Brainstorming exercise-mapping - illustrates thinking process when grouping data in a manageable set of categories based on a few sets of criteria
* tab 4: mappings - actual mappings used to map distict values in a column filed into additional summarized data column in tab 1
* tab 5: Q1 Check weather daily and Q2 - sliced and diced by various dimensions (pivot/slicer example)
* tab 6: Q3-various ways to group- donut chart
* tab 7: Q4 Stratified Answers - age , gender, hausehold income, region

#### Tableau Analysis  - Weather Checking Trends

**What Customer Behavior Shifts May Mean for the Weather Channel Established Business and 
Its Ventures in the Smartwatch Weather Apps**
* Story point 1: SAMPLE CHECKS-Good sample representation
* Story point 2: SAMPLE CHECKS-Most respondents provided the needed general info requested upfront
* Story point 3: Q1 and Q2: Most respondents reported checking the weather daily. The defaut weather app on their phone is the most common way to do so (about 23% of the time)
* Story point 4: Q3: When using a specific website, the weather channel is most used
* Story point 5: Q4: Almost 70% of respondents reported being very likely or somewhat likely to check the weather on their smart watch, if they had one.
* Story point 6: Next Interesting Step would be to learn about the most popular weather apps and why they have been succesful (opportunity to either license or emulate)

The Jupyter Notebook illustrates some basic data wrangling and visualization skills using Pandas. I am learning Python on my own and this was a good opportunity to experiment with it. 
