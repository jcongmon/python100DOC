import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (idx, row) in df.iterrows()}

txt = input("Enter a word: ").upper()
new_nato = [data_dict[c] for c in txt if c in data_dict.keys()]
print(new_nato)
