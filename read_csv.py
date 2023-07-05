print('Dit is een csv uitlees programma')

import pandas

df = pandas.read_csv('pokemon.csv')
print(df["Name"])

for r, rij in df.iterrows():
    print(r)
    print(rij["Name"])