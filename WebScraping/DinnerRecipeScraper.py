import webbrowser as wb, bs4, requests
from selenium import webdriver
from os import getcwd
from os.path import exists
import random
import re
import pandas as pd


def recipePicker(count):
    with open('recipes.csv', 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        
        if int(count) <= num_lines:
            for _ in range(int(count)):
                line_num = random.randint(0, num_lines - 1)
                split_prnt = lines[line_num].split(',')
                listing = ' : '.join(split_prnt)
                print(listing)
                
        else:
            print(f"Your number has exceeded the limit, the last line is {num_lines}")
    

cwd = getcwd()
recipePath = cwd + '\\recipes.csv'
if exists(recipePath) == False:
    url = 'https://www.simplyrecipes.com/quick-dinner-recipes-5091422'


    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    soup = bs4.BeautifulSoup(html,'html.parser')

    cards = soup.find_all(class_='card__title-text')
    links = soup.find_all('a', href=re.compile('https://www.simplyrecipes.com/'))
    recipeScrape = {'Recipe': [], 'Link' : []}
    for card, link in zip(cards,links):
            recipeScrape['Recipe'].append(card.get_text())
            recipeScrape['Link'].append(link['href'])
    df = pd.DataFrame(recipeScrape)
    df.to_csv('recipes.csv',index=False)
    
    rep_cnt = input("how many time you want to repeat it?")
    recipePicker(count=rep_cnt)

else:
    rep_cnt = input("how many time you want to repeat it?")
    recipePicker(count=rep_cnt)