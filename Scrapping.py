# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 01:29:15 2018

@author: Rakesh Gupta
"""

import pandas as pd;
from bs4 import BeautifulSoup;
from selenium import webdriver;
import time;
import datetime;

finalDataframe = pd.DataFrame()
outputFile = "Weather_hinckley.csv"
websiteUrl = "https://www.wunderground.com/history/monthly/KJMR/date/"
cityName = "Onamia"
state_code = "MN"
statename= "Minnesota"
zipcode = "55037"
webdriverChromeLocation = r"C:/Users/rakes/chromedriver_win32/chromedriver.exe"

# The year for which we need to scrape the data monthwise
for i in range(2012,2019, 1):
    # since, data is in monthly format on the Wunderground website, data is scrapped monthly.
    for k in range(1,13,1):
        # terminating and write the content of the finalDataFrame to csv file
        if k == 12 and i == 2018:
#            finalDataframe.to_csv("Weather_Hen_Jan2012_Jan2014.csv")     
            finalDataframe.to_csv(outputFile)          
        else:
            browser = webdriver.Chrome(webdriverChromeLocation) #replace with .Firefox(), or with the browser of your choice
            url = websiteUrl + str(i) + "-" + str(k) + "?req_city=" + cityName + "&req_state=" + state_code +"&req_statename=" + statename + "&reqdb.zip=" + zipcode + "&reqdb.magic=1&reqdb.wmo=99999"
            browser.get(url) #navigate to the page
            time.sleep(80)
            innerHTML = browser.execute_script("return document.documentElement.outerHTML")
            soup = BeautifulSoup(innerHTML, 'html.parser')
            browser.quit()
            table = soup.find_all(class_ = 'days')
            DayMonthSeries = pd.Series(d.find('td').text.strip() for d in table[0].find('tbody').find('tr').find_all('td')[0].find('table').find('tbody').find_all('tr'))
            
            MaxTempSeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[1].find('table').find('tbody').find_all('tr'))
            AvgTempSeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[1].find('table').find('tbody').find_all('tr'))
            MinTempSeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[1].find('table').find('tbody').find_all('tr'))
            
            MaxDewPointSeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[2].find('table').find('tbody').find_all('tr'))
            AvgDewPointSeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[2].find('table').find('tbody').find_all('tr'))
            MinDewPointSeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[2].find('table').find('tbody').find_all('tr'))
            
            MaxHumiditySeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[3].find('table').find('tbody').find_all('tr'))
            AvgHumiditySeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[3].find('table').find('tbody').find_all('tr'))
            MinHumiditySeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[3].find('table').find('tbody').find_all('tr'))
            
            MaxWindSpeedSeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[4].find('table').find('tbody').find_all('tr'))
            AvgWindSpeedSeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[4].find('table').find('tbody').find_all('tr'))
            MinWindSpeedSeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[4].find('table').find('tbody').find_all('tr'))
            
            MaxPressueSeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[5].find('table').find('tbody').find_all('tr'))
            AvgPressueSeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[5].find('table').find('tbody').find_all('tr'))
            MinPressueSeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[5].find('table').find('tbody').find_all('tr'))
            
            MaxPrecipitationSeries = pd.Series(d.find_all('td',recursive = False)[0].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[6].find('table').find('tbody').find_all('tr'))
            AvgPrecipitationSeries = pd.Series(d.find_all('td',recursive = False)[1].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[6].find('table').find('tbody').find_all('tr'))
            MinPrecipitationSeries = pd.Series(d.find_all('td',recursive = False)[2].text.strip() for d in table[0].find('tbody').find('tr').find_all('td', recursive = False)[6].find('table').find('tbody').find_all('tr'))
            
            
            
            weatherdf = pd.concat([DayMonthSeries.to_frame(), MaxTempSeries.to_frame(), AvgTempSeries.to_frame(), MinTempSeries.to_frame(), \
                       MaxDewPointSeries.to_frame(), AvgDewPointSeries.to_frame(), MinDewPointSeries.to_frame(), \
                       MaxHumiditySeries.to_frame(), AvgHumiditySeries.to_frame(), MinHumiditySeries.to_frame(), \
                       MaxWindSpeedSeries.to_frame(), AvgWindSpeedSeries.to_frame(), MinWindSpeedSeries.to_frame(), \
                       MaxPressueSeries.to_frame(), AvgPressueSeries.to_frame(), MinPressueSeries.to_frame(), \
                       MaxPrecipitationSeries.to_frame(), AvgPrecipitationSeries.to_frame(), MinPrecipitationSeries.to_frame()], axis = 1)
            
            weatherdf.drop(weatherdf.index[0], inplace = True)
            
            weatherdf.columns = ["Day", "MaxTemp", "AvgTemp", "MinTemp", \
                       "MaxDewPoint", "AvgDewPoint", "MinDewPoint", \
                       "MaxHumidity", "MaxHumidity", "MaxHumidity", \
                       "MaxWindSpeed", "AvgWindSpeed", "MinWindSpeed", \
                       "MaxPressue", "AvgPressue", "MinPressue", \
                       "MaxPrecipitation", "AvgPrecipitation", "MinPrecipitation"]
            
            weatherdf.index = weatherdf["Day"].map(lambda x: pd.to_datetime(datetime.datetime(year=i, month=k, day=int(x)), yearfirst = True).strftime("%Y-%m-%d"))
            
            weatherdf = weatherdf.iloc[:,1:]
            
            if finalDataframe.empty:
                finalDataframe = weatherdf
            else:
                finalDataframe = pd.concat([finalDataframe, weatherdf])

           























