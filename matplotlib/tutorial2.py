from matplotlib import pyplot as plt
import csv
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use("fivethirtyeight")
data = pd.read_csv("data.csv")

ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages = list()
popularity = list()

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages, popularity)



plt.xlabel("Popularity")
plt.title("Most popular languages")
# plt.legend()
plt.tight_layout()
plt.show()
