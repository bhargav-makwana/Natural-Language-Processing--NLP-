from nltk.tokenize import sent_tokenize, word_tokenize

""" Some Wordings about Natural Language Processing (NLP) """
# Tokenizing -- word tokenizing and sentence tokenizing
# Corpora - Body of text e.g. Medical journals, presidential speeches, English Language
# Lexicon - Words and their meanings

# Investor-speak differs from Regular english-speak

# When Investor says 'bull' = someone who is positive about the market
# When English speaker 'bull' = talking about the animal bull

sample_text = "Hello Mr. Makwana, how are you today? The weather is great! NLP is great to learn."

# print(sent_tokenize(sample_text))
# print(word_tokenize(sample_text))

for i in sent_tokenize(sample_text):
    print(i)