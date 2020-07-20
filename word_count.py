import re
sentence = "Geeksforgeeks,    is best @# Computer Science Portal.!!!Today is Good day? hi-hello.how do you do-do"

regex = r'[a-zA-Z0-9_-]+'
res = len(re.findall(regex, sentence))

print("No. of words in sentence is " + str(res))