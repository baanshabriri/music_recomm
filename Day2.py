import quandl
import pandas as pd
import pickle
api_key = 'MJSmRS7eQWT9WMiX2Ezp'
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][1:]

def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken = api_key)
        df.columns = [str(abbv)]
        df[abbv] = (df[abbv]-df[abbv][0]/df[abbv][0]*100.0)
        if main_df.empty:
            main_df=df
        else:
            main_df = main_df.join(df)
    pickle_out = open('fiddy_states3_rolling_pct_change.pickle','wb')
    pickle.dump(main_df,pickle_out)
    pickle_out.close()

#grab_initial_state_data()
#pickle_in = open('fiddy_states3_rolling_pct_change.pickle','rb')
#HPI_data = pickle.load(pickle_in)
#print(HPI_data)
#df2 = pd.DataFrame(HPI_data)
#print(df2.head(10))
#print(HPI_data[['TX','TX2']].head(10))
#HPI_data.plot()
#plt.legend().remove()
#plt.show()
HPI_data = pd.read_pickle('fiddy_states3_rolling_pct_change.pickle')
HPI_data['TX2'] = HPI_data['TX']*2
HPI_State_Correlation = HPI_data.corr()
TX1yr = HPI_data['TX'].resample('A').mean()
print(TX1yr.head)
print(HPI_State_Correlation)
print(HPI_State_Correlation.describe())


def HPI_benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken = api_key)
    df.columns=['United States']
    df["United States"] = (df["United States"]-df["United States"][0]/df["United States"][0]*100.0)
    return df

#fig = plt.figure()
#ax1 = plt.subplot2grid((1,1),(0,0))
benchmark = HPI_benchmark()
print(benchmark)
#HPI_data.plot(ax=ax1)
#benchmark.plot(color = 'k', ax=ax1, linewidth=10)
#plt.legend().remove()
#plt.show()
fig2=plt.figure()
ax2 = plt.subplot2grid((1,1),(0,0))
HPI_data['TX'].plot(ax=ax2)
TX1yr.plot(color='k', ax=ax2)
plt.legend().remove()
plt.show()
