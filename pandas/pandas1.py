# codes used in pandas_01.ipynb
import pandas as pd

data = pd.read_csv('./Data/sales.csv')
data.head()
data.tail()
data.shape

# pandas dataframes and series
type(data)
data.describe()

insects = ["Ants", "Cricket", "Bee"]
type(insects)

data_insects = pd.DataFrame(insects, columns=['Insects'])
data_insects

animals = {'Mammals' : ['Cow', 'Sheep', 'Lion'],
           'Reptiles' : ['Crocodile', 'Lizard', 'Snake'],
           'Insects' : ['Ants', 'Cricket', 'Bee']}
type(animals)
data_animals = pd.DataFrame(animals)
data_animals

data_animals['Mammals']
data_animals.Reptiles
type(data_animals['Mammals']) # Series
type(data_animals.Reptiles) # Series
data_animals[['Mammals', 'Reptiles']] # DataFrame

data_animals.iloc[0]
type(data_animals.iloc[0]) # Series
data_animals.iloc[[0, 1]]
type(data_animals.iloc[[0, 1]])


# indexes
data.iloc[4]
new_data = data.head()
new_data

indexes = ['One', 'Two', 'Three', 'Four', 'Five']
new_data.set_index([indexes], inplace=True)
new_data
new_data.loc['Four']
type(new_data.loc) # DataFrame
type(new_data.loc['Four']) # Series

# filtering data
data
highest_sales = (data['Sales'] > 300)
highest_sales

data.loc[highest_sales]
data.loc[highest_sales, ['Product', 'Profit', 'Sales']]
data['Product'].unique() # unique values in a column displayd as array

product = ['Green Tea', 'Lemon', 'Mint']
filt = data['Product'].isin(product)
data.loc[filt]

# updating rows and columns
data.columns.str.replace(' ', '_')
data.columns = data.columns.str.replace(' ', '_')
data.head()
data.Product_Type

data.rename(columns={'Marketing':'Trade'}, inplace=True)
data

data.loc[2, 'Total_Expenses'] = 500
data

# using 'at' better than 'loc' for single value
data.at[2, 'Total_Expenses'] = 700
data

# adding/removing rows and columns
new_column = data['Total_Expenses'] + data['Sales']
data['New_Column'] = new_column
data

data.drop(columns = ['Product', 'Market_Size'], inplace=True)
data

data.drop(index=0)

# data sorting
data.sort_values(by='Sales')
data.sort_values(by=['Sales', 'Trade'], ascending=True)
data.sort_index(ascending=False)
data.sort_index(ascending=True)
data['Market'].sort_values()
data['New_Column'].sort_values()
type(data['New_Column'].sort_values())


# grouping data
data.groupby('Sales').sum('Profit') # sum of profit for each sales value

grouped = data.groupby('State').agg({'Profit':'mean', 'Sales':'count'}) # mean profit and count of sales for each state
grouped

# cleaning and saving dataframes
data.isnull().sum() # check for null values in each column

data.dropna(inplace=True) # drop rows with null values
data.isnull().sum()

data.to_csv('New_sales.csv') # save the dataframe to a new csv file