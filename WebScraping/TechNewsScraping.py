from bs4 import BeautifulSoup
import requests
import tkinter as tk


window = tk.Tk()
window.title("Tech News")
window.geometry('720x420')
text = tk.Text(window)
text.pack()

url = 'https://techcrunch.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, features='html.parser')
title = soup.title.string
paragraphs = soup.find_all('a', class_='post-block__title__link')
for paragraph in paragraphs:
    text.insert(tk.INSERT, paragraph.text.strip(" \n\t")+'\n')
window.mainloop()