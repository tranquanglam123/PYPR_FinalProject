import matplotlib.pyplot as plt
'''month_number=[1,2,3,4,5,6,7]
new_cases=[9926,76246,681448,2336640,2835147,4226655,6942042]
plt.plot(month_number, new_cases)
plt.show()'''
month_number=[1,2,3,4,5,6,7]
new_deaths=[213,2729,37718,184064,143119,136073,165003]
plt.plot(month_number,new_deaths)
plt.title("New Reported Cases By Month(Globally)")
plt.xlabel("Month Number")
plt.ylabel("Cases")
plt.show()

