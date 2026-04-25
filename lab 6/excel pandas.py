import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#1
df = pd.read_excel("catalog_products.xlsx")
print("Форма DataFrame:", df.shape)
print("\nТипы данных:\n", df.dtypes)
print("\nПропуски:\n", df.isnull().sum())
print("\nПервые 5 строк:\n", df.head())
#2
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col], errors='raise').astype(float)
    except:
        pass
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
print(df[num_cols].isnull().sum().head())
print(df[num_cols].dtypes)

#3
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log(df['col_2'])
print(df[['total_value', 'double_stock', 'log_price']].head())

#4
electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == 'Electronics')]


#5
result = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()
result.columns = ['category', 'mean_price', 'max_price', 'total_quantity']
print(result)

#6
cols = df.select_dtypes(include='number').columns[:10]
stats = df[cols].agg(['mean', 'median', 'std']).T.reset_index()
stats.columns = ['column', 'mean', 'median', 'std']
print(stats)

#7
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()
anomalies = df[df['col_2'] > mean_price + 3 * std_price]
print(anomalies.head())

#8
cols8 = df.select_dtypes(include='number').columns[:9].tolist()
print(df[cols8].corr().round(2))

#9
plt.figure(figsize=(10, 5))
plt.hist(df['col_2'], bins=50)
plt.title('Распределение цены товаров')
plt.xlabel('Цена')
plt.ylabel('Количество товаров')
plt.grid(True)
plt.show()

#10
plt.figure()
sns.regplot(x="col_2", y="col_3", data=df)
plt.title("Цена vs Количество")
plt.xlabel("Цена")
plt.ylabel("Количество")
plt.show()

#11
df.boxplot(column='col_2', by='col_7', figsize=(10, 5))
plt.title('Распределение цены по категориям')
plt.suptitle('')
plt.xlabel('Категория')
plt.ylabel('Цена')
plt.show()

#12
sns.pairplot(df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']], hue='col_7')
plt.show()

#13
cols8 = df.select_dtypes(include='number').columns[:9].tolist()
corr = df[cols8].corr()
sns.heatmap(corr, annot=True)
plt.show()

#14
df.to_excel('catalog_analysis.xlsx', index=False)
print("Файл сохранён: catalog_analysis.xlsx")

#15
category_summary = df.groupby('col_7').agg(
    count=('col_2', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()
category_summary.columns = ['category', 'count', 'mean_price', 'total_quantity', 'mean_log_price']
print(category_summary.head())

#16
most_expensive = df.loc[df.groupby('col_7')['col_2'].idxmax(), ['col_1', 'col_2', 'col_7']]
print(most_expensive)

#17
top10 = df.nlargest(10, 'total_value')[['col_1', 'col_2', 'col_3', 'total_value']]
print(top10)

#18
bins = [0, 50, 200, 500, 1000, float('inf')]
labels = ['0-50', '50-200', '200-500', '500-1000', '>1000']
df['price_range'] = pd.cut(df['col_2'], bins=bins, labels=labels)
price_counts = df['price_range'].value_counts().sort_index().reset_index()
price_counts.columns = ['price_range', 'count']
sns.barplot(data=price_counts, x='price_range', y='count')
plt.show()

#19
category_value = df.groupby('col_7').apply(lambda x: (x['col_2'] * x['col_3']).sum()).reset_index()
category_value.columns = ['category', 'total_stock_value']
top_category = category_value.loc[category_value['total_stock_value'].idxmax(), 'category']
print(f"Категория с наибольшей стоимостью: {top_category}")
plt.bar(category_value['category'], category_value['total_stock_value'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#20
category_stats = df.groupby('col_7').agg(mean_price=('col_2', 'mean'), mean_quantity=('col_3', 'mean')).reset_index()
sns.scatterplot(data=category_stats, x='mean_price', y='mean_quantity', hue='col_7', s=100)
plt.show()

#21
std_by_category = df.groupby('col_7')['col_2'].std().sort_values().reset_index()
std_by_category.columns = ['category', 'std_price']
plt.barh(std_by_category['category'], std_by_category['std_price'])
plt.show()

#22
out_of_stock = df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']]
print(out_of_stock.head(10))

#23
top5 = df.groupby('col_7')['col_1'].count().nlargest(5).reset_index()
top5.columns = ['category', 'count']
plt.bar(top5['category'], top5['count'])
plt.show()

#24
top10_stock = df.nlargest(10, 'col_3')[['col_1', 'col_3']]
sns.barplot(data=top10_stock, x='col_3', y='col_1')
plt.show()

#25
pivot = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlOrRd')
plt.show()

#36
sns.scatterplot(data=category_stats, x='mean_price', y='mean_quantity', hue='col_7', s=100)
plt.title('Сравнение категорий по средней цене и запасу')
plt.show()

#37
std_by_category = df.groupby('col_7')['col_2'].std().sort_values().reset_index()
plt.barh(std_by_category['col_7'], std_by_category['col_2'])
plt.show()

#38
print(df[df['col_3'] == 0][['col_1', 'col_7', 'col_2']].head(10))

#39
top5 = df.groupby('col_7')['col_1'].count().nlargest(5)
top5.plot(kind='bar')
plt.show()

#40
top10 = df.nlargest(10, 'col_3')[['col_1', 'col_3']]
sns.barplot(data=top10, x='col_3', y='col_1')
plt.show()

#41
pivot = df.pivot_table(index='col_7', columns='price_range', values='col_1', aggfunc='count', fill_value=0)
sns.heatmap(pivot, annot=True, fmt='d', cmap='YlOrRd')
plt.show()

#42
sns.regplot(data=df, x='col_2', y='col_5', scatter_kws={'alpha': 0.3})
plt.title('Взаимосвязь цены и рейтинга')
plt.show()

#43
sns.pairplot(df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']], hue='col_7')
plt.show()

#44
mean_p, std_p = df['col_2'].mean(), df['col_2'].std()
mean_s, std_s = df['col_3'].mean(), df['col_3'].std()
extreme_items = df[(df['col_2'] > mean_p + 3*std_p) | (df['col_3'] > mean_s + 3*std_s)]
print(extreme_items[['col_1', 'col_2', 'col_3', 'col_7']].head())

#45
with pd.ExcelWriter('catalog_final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Данные', index=False)
    df.groupby('col_7').agg(mean_price=('col_2', 'mean'), total_quantity=('col_3', 'sum')).to_excel(writer, sheet_name='Категории')
    df.nlargest(10, 'total_value')[['col_1', 'col_2', 'col_3', 'total_value']].to_excel(writer, sheet_name='Топ10', index=False)