import nltk
from nltk.book import *

# nltk.download('gutenberg')
# nltk.download('genesis')
# nltk.download('inaugural')
# nltk.download('nps_chat')
# nltk.download('webtext')
# nltk.download('treebank')

#First 100 words
print(text1[0:100])

#count occurrences
print(text1.count('Dick'))

#length
print(len(text1))

#number of unique words
print(len(set(text1)))

#find similiar words
print(text1.similar('boat'))

#find context
print(text1.concordance('boat'))


test1 = 'ship'
test2 = 'whale'

count_text1 = text1.count(test1)
count_text2 = text2.count(test1)

count_text3 = text1.count(test2)
count_text4 = text2.count(test2)
print("Text 1: ",text1)
print("Text 2: ",text2)
print("\nTest 1 in Text 1:", count_text1)
print("\nTest 1 in Text 2:", count_text2)
print("\nTest 2 in Text 1:", count_text3)
print("\nTest 2 in Text 2:", count_text4)
