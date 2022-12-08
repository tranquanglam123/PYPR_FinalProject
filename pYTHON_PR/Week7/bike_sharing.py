import pandas as pd
day=pd.read_csv('day.csv')
import matplotlib.pyplot as plt
day['dteday']=pd.to_datetime(day['dteday'])
'''plt.plot(day['dteday'],day['temp'])
plt.xlabel('date')
plt.xticks(rotation=45)
plt.ylabel('charge')
plt.scatter(day['atemp'],day['registered'])
plt.xlabel('Attemp')
plt.ylabel('Registered')
plt.show()
correlation='positve' '''
temp_attemp_corr=day['temp'].corr(day['atemp'])
wind_hum_corr=day['windspeed'].corr(day['hum'])

plt.scatter(day['temp'],day['atemp'])
plt.title(temp_attemp_corr)
plt.xlabel('Temperature')
plt.ylabel('Feeling Temperature')
plt.show()

plt.scatter(day['windspeed'],day['hum'])
plt.title(wind_hum_corr)
plt.xlabel('Wind Speed')
plt.ylabel('Humidity')
plt.show()

