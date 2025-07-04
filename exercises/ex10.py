def count_word (sentence):
    word_list = sentence.split()
    print(word_list)
    return len(word_list)
    
user_input =input ("pls enter ure sentence here :")
num_word =count_word(user_input)
print ( f"the number of words in this sentence is : {num_word}")