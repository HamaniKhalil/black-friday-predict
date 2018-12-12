# -*- coding: UTF-8 -*-
#!/anaconda3/bin/python

import pandas as pd
import numpy as np
from time import time

# encodage
from Encoder import Encoder
from sklearn.preprocessing import minmax_scale

# partitionnement des données
from sklearn.model_selection import train_test_split

# modèles
from sklearn.linear_model import LinearRegression, LogisticRegression
from utils import train_model

# mesures de performances
from sklearn.metrics import accuracy_score,precision_score, recall_score, precision_recall_fscore_support
from sklearn.metrics import average_precision_score
from utils import show_performances

bf_df = pd.read_csv('./BlackFriday_Price_Preprocessed.csv')
bf_df.head()

product_id_encoder = Encoder.Encoder()
product_id = bf_df["Product_ID"].tolist()
product_id_encoded = product_id_encoder.encode_data(product_id)

gender_encoder = Encoder.Encoder()
gender = bf_df["Gender"].tolist()
gender_encoded = gender_encoder.encode_data(gender)

age_encoder = Encoder.Encoder()
age = bf_df["Age"].tolist()
age_encoded = age_encoder.encode_data(age)

occupation_encoder = Encoder.Encoder()
occupation = bf_df["Occupation"].tolist()
occupation_encoded = occupation_encoder.encode_data(occupation)

city_category_encoder = Encoder.Encoder()
city_category = bf_df["City_Category"].tolist()
city_category_encoded = city_category_encoder.encode_data(city_category)

years_encoder = Encoder.Encoder()
years = bf_df["Stay_In_Current_City_Years"].tolist()
years_encoded = years_encoder.encode_data(years)

martial_status_encoder = Encoder.Encoder()
martial_status = bf_df["Marital_Status"].tolist()
martial_status_encoded = martial_status_encoder.encode_data(martial_status)

product_categpry_one_encoder = Encoder.Encoder()
product_categpry_one = bf_df["Product_Category_1"].tolist()
product_categpry_one_encoded = product_categpry_one_encoder.encode_data(product_categpry_one)

product_categpry_two_encoder = Encoder.Encoder()
product_categpry_two = bf_df["Product_Category_2"].tolist()
product_categpry_two_encoded = product_categpry_two_encoder.encode_data(product_categpry_two)

product_categpry_three_encoder = Encoder.Encoder()
product_categpry_three = bf_df["Product_Category_2"].tolist()
product_categpry_three_encoded = product_categpry_three_encoder.encode_data(product_categpry_three)

X = np.column_stack((np.asarray(product_id_encoded).astype(np.object),
                     gender_encoded,
                     age_encoded,
                     occupation_encoded,
                     city_category_encoded,
                     years_encoded,
                     martial_status_encoded,
                     product_categpry_one_encoded,
                     product_categpry_two_encoded,
                     product_categpry_three_encoded))

y = bf_df["Purchase"].tolist()

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=42, shuffle=True)

print(len(X_train), " train set size.")
print(len(X_test), " test  set size.")

reg = LinearRegression()

reg.fit(X_train, y_train)

print(reg.score(X_test, y_test))
