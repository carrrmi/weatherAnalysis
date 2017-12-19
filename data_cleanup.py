import os
import pandas as pd
import numpy as np

path = '.'

weather = pd.read_csv(os.path.join(path, 'weather-check.csv'))

weather.columns = ['ID','checkDaily','howDoYouCheck','siteOrAppUsed','useSmartwatch','age','gender','income','region']
# print(weather[0:3])

# print(weather.dtypes)

categories = ['checkDaily', 'howDoYouCheck','useSmartwatch','age','gender','income','region']

for category in categories:
    weather[category] = weather[category].astype("category")


# print(weather.describe(include=['category']))

cleanedData = weather.replace("-","No Answer")

#before
# print(weather['howDoYouCheck'][0:9])
#after
# print(cleanedData['age'][0:9])

sites = cleanedData['siteOrAppUsed'].unique()
sites.sort()
# print(sites)
# print(cleanedData['howDoYouCheck'].value_counts())

selected = cleanedData[cleanedData['siteOrAppUsed'].str.contains("ipad|iphone")]

# print(selected['siteOrAppUsed'])
# print(selected['siteOrAppUsed'].count())
# print(cleanedData['siteOrAppUsed'].filter(like= 'ipad',axis=0))

saidYes =  cleanedData[cleanedData['checkDaily'] == "Yes"]
print(saidYes)

