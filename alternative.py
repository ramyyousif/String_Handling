# Training

first_string = 'I hope you are having a great day!'

second_string = ''

for i in range(len(first_string)):
    if i % 2 == 0:
        second_string += first_string[i].upper()
    else:
        second_string += first_string[i].lower()

print(second_string)

third_string = 'I hope you are having a great day!'

third_split_string = third_string.split()

modified_words = [] # Using a list instead of a string.

for i, item_2 in enumerate(third_split_string):    
    if i % 2 == 0:        
        modified_words.append(item_2.upper())    
    else:        
        modified_words.append(item_2.lower())

modified_sentence = ' '.join(modified_words)
print(modified_sentence)

