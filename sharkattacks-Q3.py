import pandas as pd

shark_attacks_df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")
shark_attacks_df = shark_attacks_df.dropna(subset=["Date"])

# 3 Are shark attacks where sharks were provoked more or less dangerous?

# Get usable values column "Fatal (Y/N)"

fatal_mapping = {"Y": "Fatal", "y": 'Fatal', "N": "Non-fatal", "N ": "Non-fatal", " N": "Non-fatal", "F": "Fatal", "n": "Non-fatal"}

for value in shark_attacks_df["Fatal (Y/N)"]:
    if value not in fatal_mapping:
        fatal_mapping[value] = 0

shark_attacks_df["Fatal (Y/N) filtered"] = shark_attacks_df["Fatal (Y/N)"].replace(fatal_mapping)
shark_attacks_filtered_per_fatality_df = shark_attacks_df[(shark_attacks_df["Fatal (Y/N) filtered"] == "Fatal") | (shark_attacks_df["Fatal (Y/N) filtered"] == "Non-fatal")]

provoked_fatal_count = len(shark_attacks_df[(shark_attacks_df["Type"] == "Provoked") & (shark_attacks_df["Fatal (Y/N) filtered"] == "Fatal")])
provoked_nonfatal_count = len(shark_attacks_df[(shark_attacks_df["Type"] == "Provoked") & (shark_attacks_df["Fatal (Y/N) filtered"] == "Non-fatal")])
unprovoked_fatal_count = len(shark_attacks_df[(shark_attacks_df["Type"] == "Unprovoked") & (shark_attacks_df["Fatal (Y/N) filtered"] == "Fatal")])
unprovoked_nonfatal_count = len(shark_attacks_df[(shark_attacks_df["Type"] == "Unprovoked") & (shark_attacks_df["Fatal (Y/N) filtered"] == "Non-fatal")])

contingency_table = pd.DataFrame({
    "Provoked": [provoked_fatal_count, provoked_nonfatal_count],
    "Unprovoked": [unprovoked_fatal_count, unprovoked_nonfatal_count]
}, index=["Fatal", "Non-fatal"])

print(contingency_table)