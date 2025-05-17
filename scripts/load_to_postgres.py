import pandas as pd

df = pd.read_csv("../data/property-transfer-statistics-june-2024-quarter.csv")

print(df.head())
print(df.columns)
print(df.info())

print('Hello, World')