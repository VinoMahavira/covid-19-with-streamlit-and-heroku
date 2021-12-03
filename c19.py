import streamlit as st
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


st.write("""
   # Covid - 19 data by Vino

   ***
""")
# dfIso = pd.read_csv('Covid-19/owid-covid-data.csv')
@st.cache
def load_data(link):
   dfVaccine = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')
   taken_field = [
      'iso_code',
      'continent',
      'location',
      'date',
      'total_cases',
      'new_cases',
      'total_deaths',
      'new_deaths',
      'positive_rate',
      'total_vaccinations',
      'people_vaccinated',
      'people_fully_vaccinated',
      'total_boosters',
      'new_vaccinations',
      'population',
      'median_age',
      'aged_65_older',
      'aged_70_older',
   ]
   dfC19 = dfVaccine[taken_field].copy()
   return dfC19
dfC19 = load_data('test')

st.write("""
   ***
   ## Data   
""")

dfC19 = dfC19.fillna(0)
dfC19['continent'] = dfC19['continent'].replace(0,'World')
continent_list = sorted(dfC19.continent.unique())
select_continent =  st.sidebar.multiselect('Country',continent_list,continent_list)
country = dfC19[(dfC19.continent.isin(select_continent))]
countries_list = sorted(country.location.unique())
select_country =  st.sidebar.multiselect('Country',countries_list,countries_list)

viewDf = dfC19[(dfC19.location.isin(select_country))]
viewDf
# countries_list = dfC19[['iso_code','location']].copy()
# countries_list = countries_list.drop_duplicates()