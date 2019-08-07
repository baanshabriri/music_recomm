import pandas
import surprise
song_df= pandas.read_csv('Song_data.csv')
print(song_df.head())
print(len(song_df))
song_grouped = song_df.groupby(['title']).agg({'listen_count':'count'}).reset_index()

grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage'] = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'title'], ascending=[0,1])
print(song_grouped.head())




