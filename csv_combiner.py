import pandas as pd
import sys

#csvs = ["fixtures/accessories.csv", "fixtures/clothing.csv", "fixtures/household_cleaners.csv"]
csvs = []

i = 1
while i < len(sys.argv):
	csvs.append(sys.argv[i])
	i += 1

dfs = []

for csv in csvs:
    file_name = csv.rpartition("/")[2]
    df = pd.read_csv(csv)
    new_col = [file_name]*df.shape[0]
    df['filename'] = new_col
    dfs.append(df)

df_all = pd.concat(dfs, ignore_index=True)
df_all.to_csv('combined.csv')
print(open('combined.csv').read())