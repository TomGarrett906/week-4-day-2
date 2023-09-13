words = ['this' , 'is', 'a', 'sentence', '.']
 #          0      1     M       -2      -1
    
def reverse_list(words):
         
    words[0], words[-1] = words[-1], words[0]
    words[1], words[-2] = words[-2], words[1]    
    
    return words

print(reverse_list(words))