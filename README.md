### List and Dictionary comprehension 
#### NATO Alphabet 
##### Introduction:
This mini-project it's about practicing using List and Dictionary comprehension, so we can write efficient code with
less line of code.
##### Example (List comprehension):
The code start with an input to take a user string and save it all with upper case, because our Nato phonetic alphabet have 
a letter column where all letters are capital.
So to convert user input string to list we can write this code:
```
for char in user_name:
    if char != " " and char.isdigit() is False:
        user_name_list.append(char)
```
As we can see it's took three lines of code but if we use list comprehension we can write it in just one line of code:
```user_name_list = [char for char in user_name if char != " " and char.isdigit() is False]```
#### Example of (Dictionary comprehension)
After we created user_name_list we need to check for each letter in NATO Alphabet data file 
So we need first to convert our Data file to Dictionary by using Pandas library.
```
nato_dict = {}
for letter in nato_df.letter:
    for (index, row) in nato_df.iterrows():
        if row.letter == letter:
            nato_dict[letter] = row.code
```
so the previous block of code loop through the nato data frame letter column
then another loop initialized to match each letter from first loop in letter in each row then assigned the letter as key
and a code as value.
But we can write the same block of code that contains 5 lines in just 3 lines of code as below:
```
nato_dict = {}
for (index, row) in nato_df.iterrows():
    nato_dict[row.letter] = row.code
```
Still Python can do more we can use dictionary comprehension to write the same block in just one line as below:
```buildoutcfg
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
```
Then last block of code from this mini project is 
Also we used list comprehension here:
From this block of code:
```
 user_name_nato = []
 for char in user_name_list:
     for (index, row) in nato_df.iterrows():
         if row.letter == char:
             user_name_nato.append(row.code)
```
To this line of code below:
```
user_name_nato = [code for letter in user_name_list for (char, code) in nato_dict.items() if letter == char]
```
