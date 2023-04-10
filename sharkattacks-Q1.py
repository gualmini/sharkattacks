import pandas as pd

shark_attacks_df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")
shark_attacks_df = shark_attacks_df.dropna(subset=["Date"])

# 1 -What are the most dangerous types of sharks to humans? We can look at the species per type of injury

# Get usable values column "Fatal (Y/N)"

fatal_mapping = {"Y": "Fatal", "y": 'Fatal', "N": "Non-fatal", "N ": "Non-fatal", " N": "Non-fatal", "F": "Fatal", "n": "Non-fatal"}

for value in shark_attacks_df["Fatal (Y/N)"]:
    if value not in fatal_mapping:
        fatal_mapping[value] = 0

shark_attacks_df["Fatal (Y/N) filtered"] = shark_attacks_df["Fatal (Y/N)"].replace(fatal_mapping)

shark_attacks_filtered_per_fatality_df = shark_attacks_df[(shark_attacks_df["Fatal (Y/N) filtered"] == "Fatal") | (shark_attacks_df["Fatal (Y/N) filtered"] == "Non-fatal")]

# Get usable values column ["Species "] in filtered dataframe

extracted_words = []
for value in shark_attacks_filtered_per_fatality_df["Species "]:
    words = str(value).split()
    try:
        shark_index = next(i for i, word in enumerate(words) if any(shark in word for shark in ['Shark', 'shark', 'Sharks', 'sharks', 'shark,']))
        if shark_index > 0:
            extracted_words.append(words[shark_index - 1].lower())
        else:
            extracted_words.append(None)
    except StopIteration:
        extracted_words.append(None)

shark_attacks_filtered_per_fatality_df.loc[:, "Extracted Words"] = extracted_words
all_species_counts = shark_attacks_filtered_per_fatality_df["Extracted Words"].value_counts()
fatal_species_counts = shark_attacks_filtered_per_fatality_df.loc[shark_attacks_filtered_per_fatality_df["Fatal (Y/N) filtered"] == "Fatal", "Extracted Words"].value_counts()
non_fatal_species_counts = shark_attacks_filtered_per_fatality_df.loc[shark_attacks_filtered_per_fatality_df["Fatal (Y/N) filtered"] == "Non-fatal", "Extracted Words"].value_counts()

#--------
print(f"Top 10 total: {all_species_counts[:10]}")
print(f"Top 10 Fatal: {fatal_species_counts[:10]}")
print(f"Top 10 Non-fatal: {non_fatal_species_counts[:10]}")

