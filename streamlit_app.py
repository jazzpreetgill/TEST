
#https://www.scrapethissite.com/pages/forms/
import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Function to get data from the website

webpage = requests.get(f"https://www.scrapethissite.com/pages/forms/").text
##‘lxml’: It’s one of the available parsers that BeautifulSoup can use to parse the HTML content. Here’s what you need to know about it:
# ‘lxml’ is a fast and efficient parser commonly used for web scraping.
# Other available parsers include ‘html.parser’ (Python’s built-in parser) and ‘html5lib’ (slower but handles broken HTML better).
soup = BeautifulSoup(webpage, 'lxml')
teachers = soup.find_all('tr')[1:]
#print(teachers)
team_name = []
year = []
wins = []
losses = []
for i in teachers:
    name = i.find_all('td')[0].text.strip()
    yr = i.find_all('td')[1].text.strip()
    wn = i.find_all('td')[2].text.strip()
    ls = i.find_all('td')[3].text.strip()
    team_name.append(name)
    year.append(yr)
    wins.append(wn)
    losses.append(ls)
data = pd.DataFrame({'Team Name': team_name,
                    'Year': year,
                    'Wins': wins,
                    'Losses': losses}) 
print(data)
st.table(data)
st.dataframe(data)
