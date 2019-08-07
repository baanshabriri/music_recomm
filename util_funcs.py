import sys
import pandas as pd
import numpy
import pickle
from collections import defaultdict, OrderedDict
from operator import *
import utils
import data_class
from data_class import Dataset

def title(s):
    return s.decode("utf8").title()

def get_songs_by_artist(data, s):
    songs = [x for x, v in data.song_sets.items() if s.lower() in x.lower()]
    return songs

def get_song(data, s):
    songs = [x for x, v in data.songs.items() if s.lower() in x.lower()]
    if len(songs) > 0:
        return songs[::5]
    else:
        return None


def read_data():
    song_df = pd.read_csv("edited_dataset.csv")
    song_df.dropna(axis=1, how='all')
    dataset = data_class.Dataset(song_df)
    print("Dataset loaded")
    return dataset


def main():
    dataset = read_data()
    print(dataset)
    #print(sorted(dataset.songs.items()))


    song = get_song(dataset, 'Bus')
    print(song)

    all_songs = get_songs_by_artist(dataset, 'john mayer')
    print(all_songs)

main()
