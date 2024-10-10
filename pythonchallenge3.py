##Andrew Aranda, Miguel Chaidez, Giovani Aguayo, Cristofer Alfaro



##1.)
text = input("Please input a text of your choice: ").lower()
text_list = list(text)

text_tuple = tuple(text)
print("Please input three letters of your choice.")
first_letter = input("First letter: ").lower()
second_letter = input("Second letter: ").lower()
third_letter = input("Third letter: ").lower()

#1.)
# check first letter 
count1 = (text_tuple.count(first_letter))
print(f"The first letter was counted {count1} times.")

# check second letter 
count2 = (text_tuple.count(second_letter))
print(f"The second letter was counted {count2} times.")

# check third letter 
count3 = (text_tuple.count(third_letter))
print(f"The third letter was counted {count3} times.")

###############################################################################################

#2.)
text_split = text.split()

word_count = len(text_split)

print(f"The total number of words inputed is {word_count}.")

###############################################################################################

#3.)
first_letter = text[:1]
last_letter = text[-1]

print(f"The first letter is {first_letter}.")
print(f"The last letter is {last_letter}.")

##################################################################################################
#4.)
text_split4 = text.split()

text_reversed4 = text_split4[::-1]

text_joined4 = " ".join(text_reversed4)
print(f"This is how the text would look like reversed: {text_joined4}.")

######################################################################################################

#5.) 
word = "python"
split2 = text.split()

if word in split2:
    print('The word "Python" is in the list.')
else:
    print('The word "Python" is not in the list.')

