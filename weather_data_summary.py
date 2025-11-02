import numpy as np  

data=np.genfromtxt('weather.csv' , delimiter=',' , skip_header=1) 
days=data[:, 0]
temp =data[:,1]
humidity=data[:,2]
rainfall=data[: , 3]


print("Average Temperature:", np.mean(temp))
print("Max Temperature:", np.max(temp))
print("Min Temperature:", np.min(temp))
print("Temperature Standard Deviation:", np.std(temp))

print("Average Humidity:", np.mean(humidity))
print("Total Rainfall:", np.sum(rainfall))

# Find hottest day
hottest_day = days[np.argmax(temp)]
print("Hottest Day:", hottest_day)

# Days with rainfall > 0
rainy_days = days[rainfall > 0]
print("Rainy Days:", rainy_days)

# Correlation between temperature & humidity
corr = np.corrcoef(temp, humidity)[0, 1]
print("Correlation between Temperature and Humidity:", corr)
