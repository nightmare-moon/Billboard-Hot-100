'''Bilboard 100 scraper'''
from bs4 import BeautifulSoup
import requests
SOURCE = requests.get('https://www.billboard.com/charts/hot-100').text
SOUP = BeautifulSoup(SOURCE, 'lxml')
SONGS = SOUP.find_all('span', attrs={'class':'chart-element__information__song'})
ARTISTS = SOUP.find_all('span', attrs={'class':'chart-element__information__artist'})

#Strip add to local dic
MUSIC = {}
for song, artist in zip(SONGS, ARTISTS):
    MUSIC[song.text] = artist.text

#Sort and print.
COUNT = -1
while COUNT > -1 + -abs(len(MUSIC)):
    OUTPUT = sorted(MUSIC.keys(), key=len)[COUNT]
    print('Song: {}      Artist: "{}!"'.format(OUTPUT, MUSIC.get(OUTPUT)))
    print('=' * 100)
    COUNT -= 1

'''
----------

    Q: Write a program (In your preferred programming language) to generate a Sorted List of Artists from “Billboard Hot 100” based on the total number of letters in their track title. 

    You can find Billboard Hot 100 list at : https://www.billboard.com/charts/hot-100

    Note:

    - Should not seek assistance from anyone.
    - You’ll be evaluated on 
    - Creativity
    - Modules used
    - Efficiency of the code during runtime.

'''
