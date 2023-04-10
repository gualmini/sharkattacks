import pandas as pd

shark_attacks_df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")
shark_attacks_df = shark_attacks_df.dropna(subset=["Date"])

# 4 - Are certain activities more likely to result in a shark attack?

activities = shark_attacks_df["Activity"].unique()
print(activities)

activities_count = shark_attacks_df["Activity"].value_counts()
print(activities_count)

top_10_mentioned_activities = shark_attacks_df["Activity"].value_counts().head(10).index.tolist()
print(top_10_mentioned_activities)
