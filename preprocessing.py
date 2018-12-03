# -*- coding: UTF-8 -*-
#!/anaconda3/bin/python

# -----------------------------------------------------------------------------------------------------------------------
# |                                                 Imports 															|
# -----------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np
import math
import exrex


DATASET = "./BlackFriday.csv"

# -----------------------------------------------------------------------------------------------------------------------
# |											    Lecture du DataSet 														|
# -----------------------------------------------------------------------------------------------------------------------
bf_df = pd.read_csv(DATASET)
bf_df.fillna(0)


# -----------------------------------------------------------------------------------------------------------------------
# |										     Encodage des catégories 													|
# -----------------------------------------------------------------------------------------------------------------------
cat1 = bf_df["Product_Category_1"].tolist()
cat2 = bf_df["Product_Category_2"].tolist()
cat3 = bf_df["Product_Category_3"].tolist()

cat_dict = {}
for cat in set(cat1):
    cat_dict[cat] = str(chr(cat + 64))

# -----------------------------------------------------------------------------------------------------------------------
# |						 Transformation des colonnes du DataFrame en Tableau de string									|
# -----------------------------------------------------------------------------------------------------------------------

for i,cat in enumerate(cat1):
    cat1[i] = cat_dict[cat]

for i,cat in enumerate(cat2):
    cat2[i] = '0' if math.isnan(cat) else cat_dict[cat]
    
for i,cat in enumerate(cat3):
    cat3[i] = '0' if math.isnan(cat) else cat_dict[cat]

# -----------------------------------------------------------------------------------------------------------------------
# |						                Concatenation des colonnes en une seule		        							|
# -----------------------------------------------------------------------------------------------------------------------
cat_all = []
for i in range(0,len(cat1)):
    cat_all.append(cat1[i]+cat2[i]+cat3[i])

# -----------------------------------------------------------------------------------------------------------------------
# |						  Création de la nouvelle colonne dans le DataFrame et suppression des 3 autres					|
# -----------------------------------------------------------------------------------------------------------------------
bf_df["Product_Category"] = pd.Series(cat_all)
bf_df = bf_df.drop(columns=['User_ID','Product_Category_1', 'Product_Category_2', 'Product_Category_3']) 

print(bf_df)

# -----------------------------------------------------------------------------------------------------------------------
# |						                        Sauvegarde du DataFrame			                                  		|
# -----------------------------------------------------------------------------------------------------------------------
bf_df.to_csv("./BlackFriday_preprocessed.csv",index=False)


# -----------------------------------------------------------------------------------------------------------------------
# |						                 Vérification des doublons par combinaisons		                           		|
# -----------------------------------------------------------------------------------------------------------------------
all_comb = list(exrex.generate('[A-R][B-R0][C-R0]'))

def containsNone(chaine, auth, unauth):
    for char in auth:
        if char not in chaine:
            return False
    for char in unauth:
        if char in chaine: return False
    return True

# Construction d'une liste reliant chaque categorie avec les combinaisons équivalentes
dict_final = {}
all_char = ['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
for x in set(cat_all):
    dict_final[x] = []
    unauthorized_char = []
    tab = []
    for char in all_char:
        if char not in list(x):
            unauthorized_char.append(char)
    for y in all_comb:
        if containsNone(y,list(x),unauthorized_char):
            tab.append(y)
    for cat_tab in tab:
        for cat in set(cat_all):
            if cat_tab==cat:
                dict_final[x].append(cat_tab)

# Vérification de l'existence de doublons dans la liste construite
for chaine in dict_final.values():
    if len(chaine) > 1:
        print("- Doublon détecté: ", chaine)