##Andrew Aranda, Miguel Chaidez, Giovani Aguayo, Cristofer Alfaro



##1.)
text = input("Please input a text of your choice: ").lower()
# text_list = list(text)
# print(text_list)
# text_tuple = tuple(text)
# print("Please input three letters of your choice.")
# first_letter = input("First letter: ").lower()
# second_letter = input("Second letter: ").lower()
# third_letter = input("Third letter: ").lower()

##1.)
# # check first letter 
# count1 = (text_tuple.count(first_letter))
# print(f"The first letter was counted {count1}.")

# # check second letter 
# count2 = (text_tuple.count(second_letter))
# print(f"The second letter was counted {count2}.")

# # check third letter 
# count3 = (text_tuple.count(third_letter))
# print(f"The third letter was counted {count3}.")

################################################################################################

# #2.)
# text_split = text.split()

# word_count = len(text_split)

# print(f"The total number of words inputed is {word_count}.")

################################################################################################

#3.)
# first_letter = text[:1]
# last_letter = text[-1]

# print(f"The first letter is {first_letter}.")
# print(f"The last letter is {last_letter}.")

##################################################################################################




# # this is the text made in to a list
# text_list = list(text)

##5.) 
split2 = text.split()

if "python" in split2:
    return True
else:
    return False