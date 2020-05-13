import re


def tokenize(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    words = dict()
    for x in text.lower():
        if x in punctuations:
            text = text.replace(x, "")
   # text = re.sub('[^A-Za-z0-9]+', ' ', text).lower()
    tokens = [t for t in text.split()]
    tokens.sort()
    for t in tokens:
        if words.get(t, 'None') == 'None':
            x = tokens.count(t)
            words.update({t: x})
    return words