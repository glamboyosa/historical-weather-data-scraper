import pandas
from pandas import Series, DataFrame
import numpy as np
import requests
from url import URLS
from bs4 import BeautifulSoup
dictionary = ''
state_name = []
state = []
avg_temp_name = []
avg_humidity_name = []
avg_pressure_name = []
month_name = []
month = []
year_name = []
year = []
avg_temp = []
avg_humidity = []
avg_pressure = []
for url in URLS:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="wt-his-title")
    results_2 = soup.find(class_="sep-t")
    if(results_2 != None):
        avg_temperature = results_2.find_all('td')[0].text[slice(
            2)]
        avgg_temp_name = results_2.find('th').text + '_Temperature'
        avgg_hum_name = results_2.find('th').text + '_Humidity'
        avgg_pressure_name = results_2.find('th').text + '_Pressure'
        avgg_hum = results_2.find_all('td', class_='sep')[0].text[slice(
            2)]
        avgg_pressure = results_2.find_all('td', class_='sep')[
            1].text.split()[0]
    if(results != None):
        data = results.text.split()

    seperator = ' '
    state_name.append("state")
    avg_temp_name.append(
        avgg_temp_name)
    avg_humidity_name.append(
        avgg_hum_name)
    avg_pressure_name.append(
        avgg_pressure_name)
    month_name.append("month")
    year_name.append("year")
    # stores the state name, average temperature, humidity and pressure in lists
    state.append(seperator.join(
        [data[0], data[1]]) if data[1] == 'Ibom' else data[0])
    avg_temp.append(np.nan if avg_temperature == 'N/A' else avg_temperature)
    avg_humidity.append(
        np.nan if avgg_hum == 'N/A' else avgg_hum)
    avg_pressure.append(
        np.nan if avgg_pressure == 'N/A' else avgg_pressure)

    if len(data) == 9:
        month.append(data[7])
        year.append(data[8])
    if len(data) == 8:
        month.append(data[6])
        year.append(data[7])
    if len(data) == 7:
        month.append(data[5])
        year.append(data[6])
# reassigning the dictionary
dictionary = {
    state_name[0]: state,
    avg_temp_name[0]: avg_temp,
    avg_humidity_name[0]: avg_humidity,
    avg_pressure_name[0]: avg_pressure,
    month_name[0]: month,
    year_name[0]: year
}
df = DataFrame(dictionary)
# data cleaning
df.dropna()
df['Average_Pressure'].replace('', np.nan, inplace=True)
df['month'].replace('24', np.nan, inplace=True)
df['year'].replace('Hours', np.nan, inplace=True)
df.dropna(subset=['Average_Pressure'], inplace=True)
df.dropna(subset=['month'], inplace=True)
df.dropna(subset=['year'], inplace=True)
# # replace 'C:\Users\Osa\Documents\weather-data.csv' with your own path
df.to_csv(r'C:\Users\Osa\Documents\weather-data.csv', index=None, header=True)
