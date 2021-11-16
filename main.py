import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
user_name = input("What is your name : ").upper()

user_name_list = [char for char in user_name if char != " " and char.isdigit() == False]
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
# for letter in nato_df.letter:
#     for (index, row) in nato_df.iterrows():
#         if row.letter == letter:
#             nato_dict[letter] = row.code

user_name_nato = [code for letter in user_name_list for (char, code) in nato_dict.items() if letter == char]
# user_name_nato = []
# user_name_nato = []
# for char in user_name_list:
#     for (index, row) in nato_df.iterrows():
#         if row.letter == char:
#             user_name_nato.append(row.code)
#
print(user_name_nato)
