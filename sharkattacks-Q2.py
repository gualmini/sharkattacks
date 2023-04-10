import pandas as pd
import re
import matplotlib.pyplot as plt
from collections import Counter

shark_attacks_df = pd.read_csv("attacks.csv", encoding = "ISO-8859-1")
shark_attacks_df = shark_attacks_df.dropna(subset=["Date"])

# 2 Are children more likely to be attacked by sharks?

shark_attacks_df["Child(Y/N)"] = ""

def classify_as_child(age):
    if isinstance(age, str):
        age = age.strip()
        match = re.match(r'^\d+', age)
        if match:
            age = int(match.group(0))
            if age <= 12:
                return "Y"
            else:
                return "N"
        elif age in ["Teen", "teen", "Teens", "20s", "30s", "40s", "50s", "60s", "adult"]:
            return "N"
    else:
        try:
            if int(age) <= 12:
                return "Y"
            else:
                return "N"
        except ValueError:
            pass
    return age

shark_attacks_df["Child(Y/N)"] = shark_attacks_df["Age"].apply(classify_as_child)


attacks_on_children = shark_attacks_df["Child(Y/N)"].value_counts()["Y"]
attacks_on_adults = shark_attacks_df["Child(Y/N)"].value_counts()["N"]
other_count = shark_attacks_df["Child(Y/N)"].value_counts().sum() - attacks_on_children - attacks_on_adults

print(f"Count of people 0-12: {attacks_on_children}")
print(f"Count of people older than 12: {attacks_on_adults}")
print(f"Count of other: {other_count}")
print(f"Total count: {attacks_on_children + attacks_on_adults + other_count}")
print(f"Attacks on people younger than 13: {round(attacks_on_children * 100 / (attacks_on_children + attacks_on_adults + other_count), 2)}")