### List and Dictionary comprehension 
#### NATO Alphabet 
##### Introduction:
This mini-project it's about practicing using List and Dictionary comprehension, so we can write efficient code with
less line of code.
##### Example (List comprehension):
The code start with an input to take a user string and save it all with upper case, because our Nato phonetic alphabet have 
a letter column where all letters are capital.
So to convert user input string to list we can write this code:

`for char in user_name:`

    `if char != " " and char.isdigit() is False:`
        user_name_list.append(char)`

As we can see it's took three lines of code but if we use list comprehension we can write it in just one line of code:
`user_name_list = [char for char in user_name if char != " " and char.isdigit() is False]`
