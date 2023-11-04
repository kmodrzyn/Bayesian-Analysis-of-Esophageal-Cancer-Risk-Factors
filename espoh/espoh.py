import pandas as pd
import numpy as np 

def split_range(x):
    if "-" in x:
        x1, x2 = x.split('-')
        return ((int(x1), int(x2)))
    else:
        x1 = x.split('+')[0]
        return ((int(x1), -1))

df = pd.read_csv('espoh.csv')

df['agegp'] = df['agegp'].apply(split_range)
df['alcgp'] = df['alcgp'].replace("0-39g/day", "0-39")
df['tobgp'] = df['tobgp'].replace("0-9g/day", "0-9")
df['alcgp'] = df['alcgp'].apply(split_range)
df['tobgp'] = df['tobgp'].apply(split_range)

df['age_low'] = df['agegp'].apply(lambda x: x[0])
df['age_high'] = df['agegp'].apply(lambda x: x[1])

df['alc_low'] = df['alcgp'].apply(lambda x: x[0])
df['alc_high'] = df['alcgp'].apply(lambda x: x[1])

df['tob_low'] = df['tobgp'].apply(lambda x: x[0])
df['tob_high'] = df['tobgp'].apply(lambda x: x[1])

df = df.drop(columns=['agegp', 'alcgp', 'tobgp'])

# df.to_csv('changed_espoh.csv') save updated data frame 

print(df)