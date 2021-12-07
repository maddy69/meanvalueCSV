import pandas as pd
df = pd.read_csv(r'C:\Users\madha\Desktop\Python\in.csv')
print(df)

#mean value
mean1 = df['Volume'].mean()
print("mean of volume: " + str (mean1))

#median value
median1 = df['Volume'].median()
print("median of volume: " + str (median1))

#standard deviation
std1 = df['Volume'].std()
print("standard deviation of volume: " + str (std1))

