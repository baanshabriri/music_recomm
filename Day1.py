"""
#Topic-1
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web

style.use('fivethirtyeight')

start = datetime.datetime(2012,1,1)
end = datetime.datetime.now()

prac_df = web.DataReader("XOM","morningstar",start,end)

prac_df.reset_index(inplace=True)
prac_df.set_index("Date", inplace = True)
prac_df = prac_df.drop("Symbol", axis =1)

print(prac_df.head())

prac_df['High'].plot()
prac_df['Low'].plot()
plt.legend()
plt.show()
------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
web_stats = {'Day':[1,2,3,4,5,6,7,8], 'Visitors':[14,12,14,55,66,44,77,88], 'Bounce_rate':[55,44,88,55,66,99,77,88]}

#Topic-2
df = pd.DataFrame(web_stats)
df.set_index("Day",inplace=True)
print(df)
print(df.tail(3))
print(df.Visitors)
df['Visitors'].plot()
plt.show()

#Topic-3
import quandl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

mydata = quandl.get('ZILLOW/Z77006_ZRISFRR')
df = pd.DataFrame(mydata)
df.columns = ['House_Prices']
print(df.head(10))
df.to_csv('house_price1.csv')
df.to_html('house_price1.html')
df.rename(columns={House_Prices:house_prices},inplace = True)
"""

import quandl
import pandas as pd
api_key = 'MJSmRS7eQWT9WMiX2Ezp'
df = quandl.get("FMAC/HPI_TX", authtoken = api_key)
df.to_csv('New_house_pricing.csv')
print(df.head(10))
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print(fiddy_states[0])
for abbv in fiddy_states[0][1][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))

