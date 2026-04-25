import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#1
df = pd.read_excel("catalog_products.xlsx")
print(df.head())
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())
#2
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = df[num_cols].astype(float)
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
text_cols = df.select_dtypes(include=['object']).columns
df = df.dropna(subset=text_cols)
print(df.isnull().sum())
#3
df["total_value"] = df["col_2"] * df["col_3"]
df["log_price"] = np.log(df["col_2"] + 1)
df["double_stock"] = df["col_3"] * 2
print(df.head())
#4
plt.figure(figsize=(8,5))
sns.histplot(df["col_2"], bins=30, kde=True)
plt.title("Price Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x=df["col_3"], y=df["col_2"])
plt.title("Price vs Quantity")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(x=df["col_7"], y=df["col_2"])
plt.xticks(rotation=45)
plt.title("Price by Category")
plt.show()
#5
price_mean = df["col_2"].mean()
price_std = df["col_2"].std()
upper_limit = price_mean + 3 * price_std
lower_limit = price_mean - 3 * price_std
anomalies = df[(df["col_2"] > upper_limit) | (df["col_2"] < lower_limit)]
print(anomalies.head())
print("Аномалия саны:", len(anomalies))
df_clean = df[(df["col_2"] <= upper_limit) & (df["col_2"] >= lower_limit)]
print(df.shape)
print(df_clean.shape)