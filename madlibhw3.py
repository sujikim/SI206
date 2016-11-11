import nltk
import random
from nltk.book import text2

nltk.download('punkt')

from nltk import word_tokenize,sent_tokenize

debug = False #True

if debug:
	print ("Getting information from file madlib_test.txt...\n")

#Using only the first 150 tokens of text2
tokens = text2[:150]
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples

#Choosing the 5 parts of speech to prompt for, including nouns
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
#Replacing nouns 15% of the time, everything else 10%
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10}


def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

final_words = []


for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))