import pandas as pd

#Creating the dataset from 2 independent datasets found on million song dataset website
"""
triplets_file = 'https://static.turi.com/datasets/millionsong/10000.txt'
songs_metadata_file = 'E:\Pandas+Matplotlib\SongCSV.csv'
song_df_1= pandas.read_table(triplets_file, header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

song_df_2 = pandas.read_csv(songs_metadata_file)
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
print(song_df.head())
song_df.to_csv("Song_data.csv")
"""
#Editing and cleaning the data

data = pd.read_csv("Song_data.csv")
data['song'] = data['title'].map(str) + " - " + data['artist_name']
data.drop(['title', 'artist_name', 'release' , 'year','Unnamed: 0','song_id'], inplace=True, axis=1)
data['listen_count'] = [10 if x > 10 else x for x in data['listen_count']]
data.rename(columns ={'user_id':'user'}, inplace=True)
print(data.head())
data.to_csv("edited_dataset.csv")