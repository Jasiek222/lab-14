from textblob import TextBlob

def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):

    blob = TextBlob(text)
    return blob.sentiment.polarity

def text_contain_word(word: str, text: str):   
    return word in text

def bubble_sort(lst):
    if lst == []:
        raise ValueError('Lista jest pusta')
    n = len(lst)
    for i in range(n - 1):
        for j in range(n-1-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j] 
    return lst