import numpy as np

table = np.genfromtxt('ABBREV.csv', delimiter=';', names=[
    'NDB_No', 'Shrt_Desc', 'Water_(g)', 'Energ_Kcal', 'Protein', 'Lipid_Tot_(g)', 'Ash_(g)', 'Carbohydrt_(g)',
    'Fiber_TD_(g)', 'Sugar_Tot', 'Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)',
    'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_mg)', 'Manganese_(mg)', 'Selenium_(µg)', 'Vit_C',
    'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Panto_Acid_mg)', 'Vit_B6_(mg)', 'Folate_Tot_(µg)',
    'Folic_Acid_(µg)', 'Food_Folate_(µg)', 'Folate_DFE_(µg)', 'Choline_Tot_ (mg)', 'Vit_B12_(µg)', 'Vit_A_IU',
    'Vit_A_RAE', 'Retinol_(µg)', 'Alpha_Carot_(µg)', 'Beta_Carot_(µg)', 'Beta_Crypt_(µg)', 'Lycopene_(µg)',
    'Lut+Zea_ (µg)', 'Vit_E_(mg)', 'Vit_D_µg', 'Vit_D_IU', 'Vit_K_(µg)', 'FA_Sat_(g)', 'FA_Mono_(g)', 'FA_Poly_(g)',
    'Cholestrl_(mg)', 'GmWt_1', 'GmWt_Desc1', 'GmWt_2', 'GmWt_Desc2', 'Refuse_Pct'
], dtype=None, encoding="utf8")
best_call = np.sort(table[1:], axis=0, order='Energ_Kcal')[-1]
best_good = np.sort(table[1:], axis=0, order='Sugar_Tot')[0]
best_prote = np.sort(table[1:], axis=0, order='Protein')[-1]
best_vitamin = np.sort(table[1:], axis=0, order='Vit_C')[0]
print(best_call[1], best_good[1], best_prote[1], best_vitamin[1], sep='\n')
