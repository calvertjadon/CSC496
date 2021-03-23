import csv
import matplotlib.pyplot as plt
from pprint import pprint
import pandas as pd
from collections import Counter

# # styling
# plt.style.use("ggplot")
plt.style.use("fivethirtyeight")
# plt.style.use("seaborn")
# plt.xkcd()

# with open("data.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     language_counter = Counter()

#     for row in csv_reader:
#         language_counter.update(row["LanguagesWorkedWith"].split(";"))

#     # languages = []
#     # popularities = []

#     # for language, popularity in language_counter.most_common(15):
#     #     languages.append(language)
#     #     popularities.append(popularity)

data = pd.read_csv("data.csv")
# ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(";"))

languages, popularity = [
    list(t) for t in zip(*language_counter.most_common(15))
]

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()  # fix formatting on smaller screens
# plt.savefig(fname="plot.png")
plt.show()
