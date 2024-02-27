import webbrowser as wb, requests,bs4
url = 'https://www.geeksforgeeks.org/matrix-manipulation-python/'
response = requests.get(url)
print (response)    
soup = bs4.BeautifulSoup(response.content, features='html.parser')
title = soup.title.string
paragraphs = soup.find_all('p')
wordToFind = '()'
x = 0
with open('output for p.txt', 'w') as file:
    for paragraph in paragraphs:
        if wordToFind in paragraph.text:
                file.write('\n ' + paragraph.text)
                print(paragraph.text)
