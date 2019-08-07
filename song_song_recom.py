import numpy as np
from collections import defaultdict
import user_user_recom
from user_user_recom import nearest_neighbours
import data_class
import similarity_metrics
from similarity_metrics import inter,intersect,jaccard,ochiai,smoothed_cosine,cosine,tfidf
import utility_funcs
from utility_funcs import title, get_song, read_data, get_songs_by_artist


def generate_song(data, song):
    print('Song-Song Recommendations for %s' %song)

    users = data.songs[song].tocsc()
    user_set = data.song_sets[song]
    user_count = len(data.user_sets)

    similarities = sims(data.song_sets, user_set, users, data.songs, data.idf)

    metrics, best = {}, set()
    inters = lambda x: inter(data.song_sets[x], user_set)
    others = similar_songs(data, song)
    similar = [(inters(other), other) for other in others]
    similar.sort(reverse=True)

    #others = similar_songs(data, song)
    for name, sim in similarities.items():
        similar = [(sim(other),other)for other in others]
        similar.sort(reverse=True)
        metrics[name] = similar
        best.update(n for _, n in similar[:10])

    output = {}
    for metric, similar in metrics.items():
        filtered = []
        for i, (score,name) in enumerate(similar):
            if name in best:
                filtered.append({'song': title(name),
                                 'score': score,
                                 'rank': i + 1})
        output[metric] = filtered
    return output




def sims(song_sets, user_set, users, songs, idf):
    """ Return lambda functions for calculating several similarity metrics. """
    return {
        'intersect': lambda x: intersect(song_sets[x], user_set),
        'ochiai': lambda x: ochiai(song_sets[x], user_set),
        'jaccard': lambda x: jaccard(song_sets[x], user_set),
        'cosine': lambda x: cosine(songs[x], users),
        'smoothed_cosine': lambda x: smoothed_cosine(songs[x], users),
        'tfidf': lambda x: tfidf(songs[x], users, idf),
    }


def find_similar_songs(data, song, min_users = 5):
    metric = generate_song(data, song)
    for metric, similar in metric.items():
        print('\n')
        print('*'*24)
        print('Metric : '+metric)
        print('Recommendations: \n')
        for x in similar:
            print(x['rank'],x['song'],x['score'])




def similar_songs(data, song):
    ret = defaultdict()
    for user in data.song_sets[song]:
        for song in data.user_sets[user]:
            title = song[2]
            rating = song[1]
            if ret.get(title) is None:
                ret[title] = (rating,1)
            else:
                ret[title] = (ret.get(title)[0] + rating, ret.get(title)[1]+1)
    ret = sorted(ret.items(), key=lambda k: k[0], reverse=True )
    top_k_users, _, _ = nearest_neighbours(ret,10)
    return top_k_users



def main():
    
    dataset = read_data()
    #song = get_song(dataset, "")
    #print(song)
    #print("Whats your song babes ?")
    #str = input()
    all_songs = get_songs_by_artist(dataset, 'metallica')

    print(all_songs)

    #find_similar_songs(dataset, song)
    find_similar_songs(dataset, all_songs[2])
main()
