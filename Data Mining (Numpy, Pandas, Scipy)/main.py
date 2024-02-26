import matika
import pandas as pd
from os import getcwd
from os.path import exists
cwd = getcwd()

# TODO : Appending to csv file 
#      : Make the excel running


matica = matika.mapGen(5,5)
pocetJednotiek = 0
pocetNul = 0
for riadok in matica:
    for prvok in riadok:
        if(prvok == 1): pocetJednotiek += 1
        elif(prvok == 0): pocetNul += 1
index = [0]

Data = {
    'Ones': pocetJednotiek,
    'Zeroes': pocetNul
}
df = pd.DataFrame(Data, index=index)
print(df)

with open((cwd + '\\output.csv'), 'a', newline='') as f:
    f.write('\n')  

if(exists(cwd + '\\output.csv')):
    existingCSVFile = (cwd + '\\output.csv')
    df.to_csv(existingCSVFile, mode='a',header=False,index=False)
df.to_csv('output.csv', index=False)
