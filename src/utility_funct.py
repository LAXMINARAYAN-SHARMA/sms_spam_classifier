from nltk.corpus import stopwords
import string
import nltk
from nltk.stem.porter import PorterStemmer


nltk.download('punkt_tab')
nltk.download('stopwords')
def data_preprocessing(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    ps=PorterStemmer()
    for i in text:
        if i.isalnum() and i not in stopwords.words('english') and i not in string.punctuation:
            y.append(ps.stem(i))
            
            
    return " ".join(y)