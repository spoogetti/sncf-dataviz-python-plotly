# %%
import pandas as pd
import plotly.express as px
import os
import dtale

# %%
chemin = "C:/Users/romai/Documents/DC5-HorsOneNote/Datavisualisation/python"
chemin_csv = os.path.join(chemin, "datasets-sncf.csv")

# %%
df_tweets = pd.read_csv(chemin_csv)
# print(df_tweets)
dtale.show(df_tweets)

# # %%
# list_colones = ["username", "name", "tweet", "date", "time", "mentions"
#                 , "urls", "photos", "replies_count", "retweets_count",
#                 "likes_count", "hashtags", "quote_url", "video", "reply_to"]
#
# df_clean = df_tweets[list_colones].copy()
# dtale.show(df_clean)
#
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