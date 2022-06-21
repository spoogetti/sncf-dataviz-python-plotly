# %% nicolas.bouchaib@first-link.fr

import pandas as pd
import plotly.express as px
import os
import dtale
import datetime

# %%
chemin = "C:/Users/romai/Documents/DC5-HorsOneNote/Datavisualisation/python"
chemin_csv = os.path.join(chemin, "objets-trouves-restitution_2022.csv")

# %%
df_objets = pd.read_csv(chemin_csv, sep=";")

# %% Histogramme 1 : Objets trouvés par mois

# list_colones = ["Date", "Gare", "Nature d'objets", "Type d'objets"]
# df_clean = df_objets[list_colones].copy()

# # %%

# month = df_clean["Date"].values
# # print(month)

# # %%

# month = [date_str.split("T")[0].split("-")[1] for date_str in month]
# month = [int(month_str) for month_str in month]
# month = [datetime.date(2022, month_int, 1).strftime("%m-%B") for month_int in month]

# # %%

# df_clean["month"] = month

# # %%

# df_clean = df_clean.sort_values(by="month", ascending=True)
# df_clean["month_count"] = df_clean.groupby("month")["month"].transform("count")
# # %%

# # dtale.show(df_clean)
# # print(df_clean)

# fig = px.bar(df_clean, x='month', y='month_count')
# fig.update_layout(
#     xaxis_title="Mois de l'année",
#     yaxis_title="Compte des objets trouvés",
# )
# export_html = os.path.join(chemin, 'found_by_month.html')
# fig.write_html(export_html)
# fig.show()
#
# # %%
# df_clean.to_excel(chemin_excel)
#
# # %%
# df_sort = df_clean.sort_values("likes_count", ascending=False).head(20)
# df_filter = df_clean.query("(likes_count > 299 or retweets_count > 99) and replies_count > 0")
#
# dtale.show(df_filter)
# # %%
# df_group = df_clean.groupby("username").sum()
# %%

# %% Histogramme 2 : Les types objets les plus perdus

list_colones = ["Type d'objets"]
df_clean = df_objets[list_colones].copy()

df_clean["object_type_count"] = df_clean.groupby("Type d'objets")["Type d'objets"].transform("count")
df_clean = df_clean.sort_values(by="object_type_count", ascending=False)

color_discrete_map = {'Optique': 'rgb(255,0,0)'}
fig = px.bar(df_clean, x='Type d\'objets', y='object_type_count', color='Type d\'objets',)


fig.update_layout(
    xaxis_title="Type d'objets",
    yaxis_title="Compte des objets trouvés",
)
# fig.show()

export_html = os.path.join(chemin, 'count_diff_items.html')
fig.write_html(export_html)