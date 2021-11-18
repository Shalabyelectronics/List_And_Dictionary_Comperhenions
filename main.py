import pandas as pd

nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
user_name = input("What is your name : ").upper()

# List comprehension:
# From this piece of code:
# user_name_list = []
# for char in user_name:
#     if char != " " and char.isdigit() is False:
#         user_name_list.append(char)
# To this below:
user_name_list = [char for char in user_name if char != " " and char.isdigit() is False]

#  Dictionary comprehension:
# From the code below:
# nato_dict = {}
# for (index, row) in nato_df.iterrows():
#     nato_dict[row.letter] = row.code
# To this below:
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# Also we used list comprehension here:
# From this block of code:
# user_name_nato = []
# for char in user_name_list:
#     for (index, row) in nato_df.iterrows():
#         if row.letter == char:
#             user_name_nato.append(row.code)
# To this line of code below:
user_name_nato = [code for letter in user_name_list for (char, code) in nato_dict.items() if letter == char]

print(user_name_nato)
