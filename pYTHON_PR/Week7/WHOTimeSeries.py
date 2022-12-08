import matplotlib.pyplot as plt
import pandas as pd
who_time_series=pd.read_csv('WHO-COVID-19-global-data.csv')
#print(who_time_series.head())
who_time_series['Date_reported']=pd.to_datetime(who_time_series['Date_reported'])
italy=who_time_series[who_time_series['Country']=='Italy']
plt.plot(italy['Date_reported'], italy['Cumulative_cases'],label='Italy')
plt.ticklabel_format(axis='y', style='plain')
#plt.title('Italy: Cumulative Reported Cases')
plt.xlabel('Date')
plt.ylabel('Cases')
india=who_time_series[who_time_series['Country']=='India']
plt.plot(india['Date_reported'],india['Cumulative_cases'],label='India')
plt.ticklabel_format(axis='y',style='plain')
plt.title('India & Italy: Cumulative Reported Cases')
plt.xlabel('Date')
plt.ylabel('Cases')
'''belarus=who_time_series[who_time_series['Country']=='Belarus']
plt.plot(belarus['Date_reported'], belarus['New_cases'], label='Belarus')
plt.ticklabel_format(axis='y',style='plain')
plt.title('Belarus:New cases')
plt.xlabel('Date')
plt.ylabel('Cases')'''
plt.legend()
plt.show()
