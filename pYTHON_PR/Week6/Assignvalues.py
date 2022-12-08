import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header=1)
tip_amount = taxi[:,12]


tip_bool = tip_amount > 50
top_tips = taxi[tip_bool, 5:14]
print(top_tips)
