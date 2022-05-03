import pandas as pd
import os
import glob
os.chdir("Spotify_Eportfolio_Data")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# add date to all files
for f in all_filenames:
    df = pd.read_csv(f)
    df.columns = df.iloc[0] 
    df = df.iloc[1:,:]
    df['YEAR'] = f[18:22]
    df['MONTH'] = f[23:25]
    df['DAY'] = f[26:28]
    df.to_csv(f, index=False, encoding='utf-8-sig')
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')

