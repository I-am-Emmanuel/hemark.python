import pandas as py

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}
temperature = py.DataFrame(temps, index=['Low', 'High'])
print(temperature)

name = temperature.loc['Low': 'High', ['Mon', 'Tue', 'Wed']]
print(name)

low = temperature.loc[['Low']]
print(low)

average = temperature.mean()
# py.set_option('precision', 2)
print(average)

low_high_temp_avg = temperature.T.mean()
print(low_high_temp_avg)

