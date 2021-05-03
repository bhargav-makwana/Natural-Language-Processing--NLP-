""" Basically Stop words used to remove low level information from the text
    Meaning of the text stays the same after removal of stop words from text."""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sample_statement = "This is an example showing off stop words filtration."
stop_words = set(stopwords.words('english'))
words = word_tokenize(sample_statement)
filtered_statement = []

for w in words:
    if w not in stop_words:
        filtered_statement.append(w)
print(filtered_statement)

# One-liner for above code
filtered_statement = [w for w in words if w not in stop_words]
print(filtered_statement)

# ------------------------------------------------------------------------------------------------
# But we do not always remove stop words

review_statement = "The movie was not good at all."
words = word_tokenize(review_statement)
stop_words = set(stopwords.words('english'))

filtered_review = []
for w in words:
    if w not in stop_words:
        filtered_review.append(w)

print(filtered_review)

""" For example,    Movie review: “The movie was not good at all.”
                    Text after removal of stop words: “movie good”
    We can clearly see that the review for the movie was negative. 
    However, after the removal of stop words, the review became positive, which is not the reality. 
    Thus, the removal of stop words can be problematic here. """

""" Reference Links
    1. https://towardsdatascience.com/text-pre-processing-stop-words-removal-using-different-libraries-f20bac19929a
    2. https://www.youtube.com/watch?v=w36-U-ccajM&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&index=2
"""