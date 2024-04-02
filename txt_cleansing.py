import pandas as pd
import nltk
from nltk.corpus import stopwords
import string

# Sample data: a simple DataFrame with a column of text
data = {'text': [ 'Data cleansing ']}
df = pd.DataFrame(data)

# Convert text to lowercase
df['cleaned_text'] = df['text'].str.lower()

# Remove punctuation
df['cleaned_text'] = df['cleaned_text'].str.translate(str.maketrans('', '', string.punctuation))

# Remove stopwords
stop = stopwords.words('english')
df['cleaned_text'] = df['cleaned_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))

print(df[['text', 'cleaned_text']])