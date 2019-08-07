from utility_funcs import read_data, get_random_user
import numpy
from collections import defaultdict
from operator import *


def similar_user_songs(data, user, k=10):
    user_songs = [z for x,y,z in data.user_sets.get(user)]

    user_set = set(user_songs)
    print('User:{0}'.format(str(user)))
    print_songs(user_songs[:k])

    #finding k most similar users
    similar_users = most_similar_users(data,user_set,k)

    #gettting  k closest items
    top_user,top_rating,top_sum = k_closest_songs(data, similar_users)

    return top_user, top_rating, top_sum




def print_songs(songs):
    print('\n Songs:')
    print('*'*25)
    for song in songs:
        print(song)
    print('\n')



def k_closest_songs(data, users):
    ret = defaultdict()
    for u in users:
        for song in data.user_sets[u]:
            title = song[2]
            listen_count = song[1]
            if ret.get(title) is None:
                ret[title] = (listen_count,1)
            else:
                ret[title] = (ret.get(title)[0]+ listen_count, ret.get(title)[1] +1)
    ret = sorted(ret.items(), key=lambda v: v[0], reverse=True)
    #print(ret)
    ret = nearest_neighbours(ret, 10)
    return ret



def nearest_neighbours(candidates, k):
    try:
        nearest_neighbours = [(title, listen_count[0], listen_count[1], listen_count[0] / listen_count[1]) \
                for title, listen_count in candidates]
    except TypeError:
        try:
            nearest_neighbours = [(title, listen_count[0], listen_count[1], listen_count[0] / listen_count[1]) \
                    for title, listen_count in candidates.items() if not numpy.isnan(title)]
        except TypeError:
            pass

    popular_users_count = sorted(nearest_neighbours, key=itemgetter(2, 1), reverse=True)
    count_popular_users = sorted(nearest_neighbours, key=itemgetter(1, 2), reverse=True)
    best_score = sorted(nearest_neighbours, key=itemgetter(3), reverse=True)
    top_k_users = [title for title, point, people, avg in popular_users_count][:k]
    top_k_count = [title for title, point, people, avg in count_popular_users][:k]
    top_k_score = [title for title, point, people, avg in best_score][:k]
    return top_k_users, top_k_count, top_k_score



def most_similar_users(data,user_set,k):
    sims = defaultdict()
    for user, songs in data.user_songs.items():
        num_songs =len(songs)
        other_songs = songs - user_set
        left = num_songs - len(other_songs)
        if left > 0 and other_songs is not []:
            sims[user] = (left, other_songs)

    k_closest = sorted(sims, key=lambda x: x[0], reverse= True)

    ret = list()
    for user in k_closest:
        ret.append(user)
    return ret


def main2():
    dataset = read_data()
    user = get_random_user(dataset)

    # user-user recommendation
    top_user, top_rating, top_sum = similar_user_songs(dataset, user)

    print("Top similar user recommendations:")
    print_songs(top_user)

    print("Top rated item recommendations:")
    print_songs(top_rating)

    print("Top scored item recommendations:")
    print_songs(top_sum)



'''

dataset = read_data()
user = get_random_user(dataset)
user_songs = [z for x,y,z in dataset.user_sets.get(user)]
user_set = set(user_songs)
print(dataset.user_songs)
#top_user, top_rating, top_sum = similar_user_songs(dataset, user)

arr = most_similar_users(dataset,user_set,10)
print(arr)

closest_songs = k_closest_songs(dataset,arr)
print(closest_songs)
ret = defaultdict()
for users in arr:
    for song in dataset.user_sets[user]:
        title = song[2]
        listen_count = song[1]
        print(song)
        print(listen_count)
        if ret.get(title) is None:
            ret[title] = (listen_count, 1)
        else:
            ret[title] = (ret.get(title)[0]+ listen_count, ret.get(title)[1] +1)

print(ret)

'''