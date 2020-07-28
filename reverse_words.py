import re
def reverse_words(sentence):
    #print(sentence)
    words = sentence.split() #split function is used to split sentences into word
    print(words)
    rev_word = " ".join(reversed(words)) #join is used to join elements of array with special character
    print(rev_word)


sentence = "hello i am revati"
reverse_words(sentence)

