import pandas as pd
import matplotlib.pyplot as plt

bike=pd.read_csv('day.csv')
bike['dteday']=pd.to_datetime(bike['dteday']
                              )
wkd=['Non-Working Day','Working Day']
'''casual_avg=[1371,607]
plt.bar(wkd, casual_avg)
plt.show()

plt.bar(x=[1,2,3,4],height=[10,20,30,80])
plt.show()'''
plt.hist(bike['cnt'])
plt.show()
