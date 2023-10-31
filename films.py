#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from pprint import pprint
url = 'https://raw.githubusercontent.com/yupest/nto/master/%D0%9D%D0%A2%D0%98-2022/films/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('div', class_='movie-head')
films = {}
for film in quotes:
    title = film.find("h1").text.split(" ")[1:]
    title = list(map(lambda word: word+" ",title))
    title = "".join(title)[:-1]
    poster_url = film.find("div", class_="movie-ava").find("img")["src"]
    info = film.find("ul",class_="info")
    genres = list(map(lambda genreLi: genreLi.text,info.find_all("li",class_="genre")))
    rate = info.find("li",class_="").text
    stat_movie=film.find_all("div","stat-movie")[1].find("ul")
    text_emotions =list(map(lambda em:em.text, stat_movie.find_all("li", class_="emotion")))
    rate_emotions = stat_movie.find_all("li",class_="spo")
    rate_emotions = map(lambda spo: spo.find("div"),rate_emotions)
 
    rate_emotions = list(map(lambda rate: float(rate.text),rate_emotions))
    emotions = list(zip(text_emotions,rate_emotions))
 
    films[title]={
    "poster_url":poster_url,
    "genres":genres,
    "rate_film":rate,
    "emotion_rates":emotions
 
 
    }
pprint(films)


# In[ ]:




