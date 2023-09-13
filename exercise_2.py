'''Exercise #2
Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.

Should output:
{'a': 5,
'abstract': 1,
'an': 3,
'array': 2, ... etc...'''


a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def distinct_words(a_text):
    distinct_dict = {} #Create empty dictionary
    distinct_list = ['a','abstract','an','array'] #Set our words we want to add

    words = a_text.split() #Split the text up so we can index one word at a time

    for word in words:  #Now to check one word 
        if word in distinct_list: #If its it the list of words we want to add
            if word not in distinct_dict: #Check our dictionarey
                distinct_dict[word] = 1 #If not in there, add it
            else:
                distinct_dict[word] += 1 #or if already have one, add another.

    return distinct_dict 

print(distinct_words(a_text))