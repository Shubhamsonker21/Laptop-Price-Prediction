import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path= r"C:\Users\shubham sonker\Downloads\laptop\laptop.csv"
data = pd.read_csv(file_path)

data.head()

data.info()

data.isnull().sum()

data.isnull().mean()*100

import missingno as msno

msno.matrix(data)

data.drop(columns=['Unnamed: 0.1','Unnamed: 0'],inplace=True)

data.dropna(inplace=True)

data.info()

data.head()

data['Price'] = data['Price'].astype(int)

data.info()

data['Ram'] = data['Ram'].str.replace('GB',' ')

data['Weight'] = data['Weight'].str.replace('kg',' ')

data.info()

data['Weight'] = data['Weight'].replace('?', np.nan)

data['Ram'] = data['Ram'].astype('int')
data['Weight'] = data['Weight'].astype('float')

data.info()

data.head()

data['Company'].value_counts().plot(kind='bar')

data.OpSys.unique()

data['OpSys'].value_counts().plot(kind='bar')

def segment(catcher):
  if catcher == 'Windows 10' or catcher == 'Windows 7' or catcher=='Windows 10 S':
    return 'Windows'
  elif catcher == 'macOS' or catcher == 'Mac OS X':
    return 'MacOS'
  else:
    return 'Linx/Android/Chrome'

data['OP System'] = data['OpSys'].apply(segment)

data['OP System'].value_counts().plot(kind='bar')

sns.barplot(x=data['OP System'], y=data['Price'])

data.drop(columns=['OpSys'],inplace=True)

data.head()

plt.figure(figsize=(15, 6))
data['Gpu'].value_counts().plot(kind='bar',)
plt.xticks(rotation=90)
plt.show()

data['Gpu'].value_counts()

data['Cpu'] = data['Cpu'].apply(lambda x:' '.join(x.split()[0:3]))

data['Cpu'].value_counts()

def word_catcher(word):
  if word == 'Intel Core i7' or word == 'Intel Core i5' or word == 'Intel Core i3':
    return word
  if word.split()[0] == 'Intel':
    return 'Other_Intel'
  else:
    return 'AMD_Processor'

data['Cpu'] = data['Cpu'].apply(word_catcher)

data['Cpu'].value_counts().plot(kind='bar')

sns.barplot(x=data['Cpu'], y=data['Price'])

data.head()

data['Gpu'].value_counts()

def pick_list(word):
  if word.split()[0]=='Intel':
    return 'Intel'
  elif word.split()[0]=='Nvidia':
    return 'Nvidia'
  else:
    return 'AMD'

data['Gpu'] = data['Gpu'].apply(pick_list)

data['Gpu'].value_counts().plot(kind='bar')

data['Gpu'].value_counts()

data.info()

data.head()

data['ScreenResolution'].value_counts()

data['Touchscreen'] = data['ScreenResolution'].apply(lambda x:1 if 'Touchscreen ' in x else 0 )

data['Touchscreen'].value_counts().plot(kind='bar')

sns.barplot(x=data["Touchscreen"], y= data['Price'])

data['IPS'] = data['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0 )

data['IPS'].value_counts().plot(kind='bar')

sns.barplot(x=data["IPS"], y= data['Price'])

data.sample(5)

new = data['ScreenResolution'].str.split('x',n=1,expand=True)

data['x_res']= new[0]
data['y_res']= new[1]

data['x_res'] = data['x_res']
data['y_res'] = data['y_res']

data.head()

data['x_res'] = data['x_res'].str.extract(r'(\d{4})$')

data.head()

data['x_res'] = data['x_res'].astype(int)
data['y_res'] = data['y_res'].astype(int)

data['Inches'].unique()

data['Inches'].info()

data.info()

data['Inches'] = pd.to_numeric(data['Inches'], errors='coerce')

data['ppi'] =(((data['x_res']**2 + data['y_res']**2)**0.5) / data['Inches'].astype(float))

data.head()

data.drop(columns=['ScreenResolution','x_res','y_res'],inplace=True)

data.drop(columns=['Inches'],inplace=True)

data.head()

data.corr()['Price']

data.replace('?', np.nan, inplace=True)

data['Memory'].value_counts().plot(kind='bar')

data['Memory'].value_counts()

data.isna().sum()

nan_memory = data[data['Memory'].isna()]
print(nan_memory)

nan_weight = data[data['Weight'].isna()]
print(nan_weight)

nan_ppi = data[data['ppi'].isna()]
print(nan_ppi)

data['Memory'].fillna(data['Memory'].mode(), inplace=True)

data['Weight'].fillna(data['Weight'].mean(), inplace=True)

data['ppi'].fillna(data['ppi'].mean(), inplace=True)

data.isna().sum()

nan_memory = data[data['Memory'].isna()]
print(nan_memory)

data.loc[data['Memory'].isna(), 'Memory'] = '128GB SSD'

data.isna().sum()

data['Memory'].value_counts()

data['SSD_size'] = data['Memory'].str.extract(r'(\d+)GB\sSSD').fillna(0).astype(int)
data['HDD_size'] = data['Memory'].str.extract(r'(\d+)\.?\d*\s?TB\sHDD').fillna(0).astype(float) * 1000
data['Flash_Storage_size'] = data['Memory'].str.extract(r'(\d+)GB\sFlash\sStorage').fillna(0).astype(int)
data['Hybrid_size'] = data['Memory'].str.extract(r'(\d+\.\d+)TB\sHybrid').fillna(0).astype(float) * 1000

data.head()

data.corr()['Price']

data.drop(columns=['Hybrid_size','Flash_Storage_size','Memory'],inplace=True)

data.head()

data.info()

data.isnull().sum()

sns.distplot(data['Price'])

sns.distplot(np.log(data['Price']))

x = data.drop(columns='Price')
y = np.log(data['Price'])

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

data.head(1)

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6]),
                                        ],remainder='passthrough')
step2 = LinearRegression()
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
print('R2_score', r2_score(y_test,y_pred))
print('Mae_score', mean_absolute_error(y_test,y_pred))

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6]),
                                        ('scaler',StandardScaler(),[3,5,7,8,9,10,11]),
                                        ],remainder='passthrough')
step2 = LinearRegression()
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
print('R2_score', r2_score(y_test,y_pred))
print('Mae_score', mean_absolute_error(y_test,y_pred))

from sklearn.model_selection import cross_val_score
step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'),[0,1,2,4,6]),

                                        ],remainder='passthrough')
step2 = RandomForestRegressor(max_depth = 30,
                              max_features = 0.06,
                              max_samples = 0.9,
                              n_estimators = 85)
pipe_random_forest = Pipeline([('step1', step1),
                ('step2', step2)])


pipe_random_forest.fit(x_train,y_train)

y_pred = pipe_random_forest.predict(x_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

# Create a DataFrame to store the metrics results
metrics_df = pd.DataFrame({'RandomForest_Metric': ['R2 Score', 'Mean Absolute Error', 'Root Mean Squared Error'],
                           'Value': [r2, mae, rmse]})

print(metrics_df)

metrics_df

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6]),
                                         ('scaler',StandardScaler(),[3,5,7,8,9,10,11]),],remainder='passthrough')
step2 = RandomForestRegressor(n_estimators=170,
                              random_state=3,
                              max_samples=0.5,
                              max_depth=15,
                              max_features=0.75)
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
print('R2_score', r2_score(y_test,y_pred))
print('Mae_score', mean_absolute_error(y_test,y_pred))

#CREATING PARAMETERS FOR TUNING
n_estimators=[15,30,45,60,75,100,]
max_samples=[0.15,0.30,0.45,0.60,0.75,0.85,]
max_depth=[5,10,20,30,None]
max_features=[0.40,0.50,0.60,0.80,0.90]

#CREATING OBJECT OF RandomForest
rf=RandomForestRegressor()

# #CREATING PIPELINE FOR OneHotEncoder AND INITIALIZING PARAMETERS.
# from sklearn.model_selection import GridSearchCV
# step1 = ColumnTransformer(transformers=[
#                                         ('onehotencoder',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'),[0,1,2,4,6]),

#                                         ],remainder='passthrough')
# rf=RandomForestRegressor()
# pipeline = Pipeline([
#     ('onehotencoder',step1),
#     ('rf', rf)
# ])

# param_grid={ 'rf__n_estimators': n_estimators,
#     'rf__max_samples': max_samples,
#     'rf__max_depth': max_depth,
#     'rf__max_features': max_features}

# print(param_grid)

# rf_grid=GridSearchCV(estimator=pipeline,param_grid=param_grid,cv=5,verbose=2,n_jobs=-1)
# rf_grid.fit(x_train,y_train)

# # OUT OF ALL PARAMETERS THESE ARE THE BEST ONES.
# rf_grid.best_params_

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6])],remainder='passthrough')
step2 = RandomForestRegressor(n_estimators=60,
                              random_state=3,
                              max_samples=0.85,
                              max_depth=30,
                              max_features=0.9)
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)


metrics_data = pd.DataFrame({'Tuned_RandomForest_Metric': ['R2 Score', 'Mean Absolute Error', 'Root Mean Squared Error'],
                           'Value': [r2, mae, rmse]})

print(metrics_data)

metrics_data

#CREATING PARAMETERS FOR TUNING
n_estimators=[100,90,80]
max_samples=[0.60,0.75,0.85,]
max_depth=[20,30,None]
max_features=[0.60,0.80,0.90]

# #CREATING PIPELINE FOR OneHotEncoder AND INITIALIZING PARAMETERS.
# from sklearn.model_selection import GridSearchCV
# step1 = ColumnTransformer(transformers=[
#                                         ('onehotencoder',OneHotEncoder(sparse_output=False,drop='first',handle_unknown='ignore'),[0,1,2,4,6]),

#                                         ],remainder='passthrough')
# rf=RandomForestRegressor()
# pipeline = Pipeline([
#     ('onehotencoder',step1),
#     ('rf', rf)
# ])

# param_grid={ 'rf__n_estimators': n_estimators,
#     'rf__max_samples': max_samples,
#     'rf__max_depth': max_depth,
#     'rf__max_features': max_features}

# print(param_grid)

# rf_grid=GridSearchCV(estimator=pipeline,param_grid=param_grid,cv=5,verbose=2,n_jobs=-1)
# rf_grid.fit(x_train,y_train)

# # OUT OF ALL PARAMETERS THESE ARE THE BEST ONES.
# rf_grid.best_params_

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6])],remainder='passthrough')
step2 = RandomForestRegressor(n_estimators=80,
                              random_state=3,
                              max_samples=0.75,
                              max_depth=None,
                              max_features=0.8)
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)


metrics_data2 = pd.DataFrame({'Tuned_RandomForest_Metric2': ['R2 Score', 'Mean Absolute Error', 'Root Mean Squared Error'],
                           'Value': [r2, mae, rmse]})

print(metrics_data2)

metrics_data2

step1 = ColumnTransformer(transformers=[
                                         ('onehotencoder',OneHotEncoder(sparse=False,drop='first'),[0,1,2,4,6]),
                                         ('scaler',StandardScaler(),[3,5,7,8,9,10,11]),],remainder='passthrough')
step2 = GradientBoostingRegressor(n_estimators=500
                            )
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
y_pred = pipe.predict(x_test)
print('R2_score', r2_score(y_test,y_pred))
print('Mae_score', mean_absolute_error(y_test,y_pred))
print('Rmse_score', np.sqrt(mean_squared_error(y_test,y_pred)))

import pandas as pd


ASUS_ROG_Strix_G15 = {
    'Company': 'ASUS',
    'TypeName': 'Gaming',
    'Ram': 16,
    'Weight': 1.59,
    'Touchscreen': 0,
    'IPS': 0,
    'ppi': 120.27,
    'Cpu': 'AMD Processor',
    'OP System': 'Windows',
    'SSD_size': 0,
    'HDD_size': 256,
    'Gpu': 'NVIDIA'}
lenovo_specs = {
    'Company': 'Lenovo',
    'TypeName': 'Notebook',
    'Ram': 16,
    'Weight': 2.4,
    'Touchscreen': 1,
    'IPS': 1,
    'ppi': 200,
    'Cpu': 'Intel Core i7',
    'OP System': 'Windows',
    'SSD_size': 1000,
    'HDD_size': 0,
    'Gpu': 'NVIDIA'
}

macbook_air_specs = {
    'Company': 'Apple',
    'TypeName': 'Ultrabook',
    'Ram': 8,
    'Weight': 1.29,
    'Touchscreen': 0,
    'IPS': 1,
    'ppi': 178,
    'Cpu': 'Intel Core i7',
    'OP System': 'MacOS',
    'SSD_size': 256,
    'HDD_size': 0,
    'Gpu': 'Intel'
}
CHUWI_HeroBook = {
    'Company': 'CHUWI',
    'TypeName': 'Netbook',
    'Ram': 6,
    'Weight': 1.38,
    'Touchscreen': 0,
    'IPS': 0,
    'ppi': 120,
    'Cpu': 'Other_Intel',
    'OP System': 'Windows',
    'SSD_size': 256,
    'HDD_size': 0,
    'Gpu': 'Intel'
}



ASUS_ROG_Strix_G15 = pd.DataFrame([ASUS_ROG_Strix_G15])
lenovo_df = pd.DataFrame([lenovo_specs])
macbook_air_df = pd.DataFrame([macbook_air_specs])
CHUWI_HeroBook = pd.DataFrame([CHUWI_HeroBook])

combined_df = pd.concat([ASUS_ROG_Strix_G15, lenovo_df, macbook_air_df,CHUWI_HeroBook], ignore_index=True)

print(combined_df)

step1 = ColumnTransformer(transformers=[
                                        ('onehotencoder',OneHotEncoder(sparse=False,drop='first',handle_unknown='ignore'),[0,1,2,4,6])],remainder='passthrough')
step2 = RandomForestRegressor(n_estimators=80,
                              random_state=3,
                              max_samples=0.75,
                              max_depth=None,
                              max_features=0.8)
pipe = Pipeline([('step1', step1),
                ('step2', step2)])
pipe.fit(x_train,y_train)
predictions = pipe.predict(combined_df)
# np.exp transformation
actual_prices = np.exp(predictions)
combined_df['Predicted_Price'] = actual_prices
print(combined_df)

#Lenovo LOQ 2024 PRICE = ₹1,02,990    #newly_launched
#macbook_air price = 70000
#ASUS_ROG_Strix_G15 PRICE = 70,323
#CHUWI HeroBook Pro = 15,644.48

"""#Questions to Explore

# Which features have the most significant impact on laptop prices?
In analyzing the factors influencing laptop prices, several key features emerged as significant determinants.

*  Touchscreen and IPS Display: Laptops equipped with Touchscreen functionality and IPS display technology tend to command higher prices. These features enhance user experience and visual quality, resulting in a price premium of approximately 20% compared to laptops without these features.

*  Storage Configuration: The type and capacity of storage components, particularly SSDs (Solid State Drives), play a crucial role in pricing. Laptops with larger SSD capacities or high-speed SSDs are often priced higher due to their faster data access and improved system responsiveness.

* Graphics Processing Unit (GPU): The presence of a dedicated GPU, especially from reputable brands such as Nvidia, contributes significantly to a laptop's price. Laptops with Nvidia graphics cards are particularly sought after for gaming, graphic design, and video editing purposes, leading to a price premium compared to integrated graphics solutions and GPUs from other manufacturers.
"""

sns.barplot(x=data["Touchscreen"], y= data['Price'])

sns.barplot(x=data["IPS"], y= data['Price'])

sns.barplot(x=data["SSD_size"], y=data['Price'])
plt.xticks(rotation=90)
plt.show()

sns.barplot(x=data['Gpu'], y=data['Price'])

data.corr()['Price']

"""# Can the model accurately predict the prices of laptops from lesser-known brands?

After conducting predictions on laptops from lesser-known brands, the model achieved an accuracy rate of approximately 50%. While this accuracy level may seem moderate, it is important to consider the context of the analysis.

The limited availability of data for lesser-known brands poses a significant challenge to the model's predictive capabilities. With fewer observations to learn from, the model may struggle to generalize effectively to unseen instances from these brands. As a result, the achieved accuracy reflects the inherent difficulty in accurately predicting prices for laptops from lesser-known brands.

Moving forward, it is crucial for the organization to continue gathering data, particularly from lesser-known brands, to improve the model's performance. With a more extensive and diverse dataset, the model can better capture the nuances and variations in laptop prices across different brands, leading to enhanced predictive accuracy.

In conclusion, while the current accuracy rate may be modest, it serves as a starting point for further refinement and improvement. By prioritizing data collection efforts and continuously refining the modeling approach, the organization can strive towards achieving higher accuracy levels in predicting prices for laptops from lesser-known brands.
"""

#Lenovo LOQ 2024 PRICE = ₹1,02,990
#macbook_air price = 70000
#ASUS_ROG_Strix_G15 PRICE = 70,323
#CHUWI HeroBook Pro = 15,644.48   #Lesser_known_brand
combined_df

"""#Does the brand of the laptop significantly influence its price?
Yes, the brand of a laptop can have a significant influence on its price. Brands with a strong reputation and brand equity, such as Apple, often command premium prices for their products. This price premium is primarily attributed to factors such as brand perception, reputation for quality, and consumer loyalty.

For example, laptops with similar specifications to those offered by Apple may be available at lower price points from other brands. However, despite comparable hardware specifications, Apple laptops tend to maintain higher price tags due to the brand's perceived value and status in the market.

"""

sns.barplot(x=data["Company"], y= data['Price'])
plt.xticks(rotation=90)
plt.show()

"""#How well does the model perform on laptops with high-end specifications compared to budget laptops?
The model demonstrates superior performance when predicting prices for laptops with high-end specifications compared to budget laptops. With an accuracy exceeding 87% on high-end laptops, the model showcases its effectiveness in accurately estimating prices for premium devices.

This higher accuracy can be attributed to several factors. High-end laptops typically feature advanced components, such as powerful processors, ample RAM, dedicated graphics cards, and larger SSD storage capacities. These specifications provide more distinct patterns and correlations in the data, enabling the model to make more precise predictions.
"""

#Lenovo LOQ 2024 PRICE = ₹1,02,990    #high-end specifications
#macbook_air price = 70000
#ASUS_ROG_Strix_G15 PRICE = 70,323
#CHUWI HeroBook Pro = 15,644.48
combined_df

"""#What are the limitations and challenges in predicting laptop prices accurately?
The accurate prediction of laptop prices poses several limitations and challenges for models. One of the primary limitations is the availability of data. Despite efforts to collect comprehensive datasets, the quantity and quality of available data may still be insufficient to capture the full range of factors influencing laptop prices. Limited data may result in model biases, reduced predictive accuracy, and challenges in generalizing to unseen instances.

#How does the model perform when predicting the prices of newly released laptops not present in the training dataset?
To evaluate the model's performance on predicting prices for newly released laptops, we conducted tests on a recently launched laptop not present in the training dataset. The actual price of the laptop was ₹1,02,990, while the model predicted a price of ₹1,13,281.

This outcome demonstrates the model's ability to provide reasonably accurate price predictions for laptops not included in the training dataset. Despite not having prior exposure to the specific features and specifications of the newly released laptop, the model generated a prediction close to the actual price.
"""

#Lenovo LOQ 2024 PRICE = ₹1,02,990    #Newly Released
#macbook_air price = 70000
#ASUS_ROG_Strix_G15 PRICE = 70,323
#CHUWI HeroBook Pro = 15,644.48
combined_df















