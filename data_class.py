from collections import defaultdict

import pandas as pd
from numpy import zeros, array
from scipy.sparse import csr_matrix


import data


class Dataset(object):
    def __init__(self, data_set):

        self.data = data_set

        # creating set of users that have listened to a particular song..
        self.song_sets = dict((song, set(users)) for song, users in self.data.groupby('song')['user'])

        # creating set of songs that a user has listened to...
        self.user_songs = dict((user, set(songs)) for user, songs in self.data.groupby('user')['song'])

        self.user_sets = self.data.set_index('user').apply(tuple, 1).groupby(level = 0).agg(lambda x: list(x.values)).to_dict()

        #mapping user -> ids
        userids = defaultdict(lambda : len(userids))
		songids = defaultdict(lambda : len(songids))

        self.data['user_id'] = self.data['user'].map(userids.__getitem__)
        self.data['song_id'] = self.data['song'].map(songids.__getitem__)

        # creating a sparse vector for each song, user
        self.songs = dict((song,csr_matrix((array(group['listen_count']),(zeros(len(group)),group['user_id'])),shape=[1, len(userids)]))for song, group in self.data.groupby('song'))

        self.users = dict((user,csr_matrix((array(group['listen_count']),(zeros(len(group)),group['song_id'])),shape=[1, len(songids)]))for user, group in self.data.groupby('user'))

        N = len(self.songs)

        #average count of plays per song
        self.average_plays = self.data['listen_count'].sum() / float(N)


def read_data():
    song_df = pd.read_csv("edited_dataset.csv")
    song_df.dropna(axis=1, how='all')
    dataset = Dataset(song_df)
    print(dataset.user_sets)


read_data()