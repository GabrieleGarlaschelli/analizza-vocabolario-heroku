from AnalizzaVocabolario.services.SplitText import tokenize

CONST_MAX_WORD_LEN = 26
CONST_LESS_15_COMPLEX = 0.5
CONST_GREAT_15_COMPLEX = 1.0


def calculateIC(text):
    dividendo = 0
    divisore = 0
    total_frequency = 0
    frequency_complex = 0
    key_to_delete = []
    words = tokenize(text)
    for word,frequency in words.items():
        if(len(word) < 3):
            key_to_delete.append(word)
    for key in key_to_delete:
        del words[key]
    for word,frequency in words.items():
        singleIC = calculateSingleWordIC(word)
        if(singleIC<15):
            dividendo += singleIC
            divisore += CONST_LESS_15_COMPLEX
        else:
            dividendo += singleIC
            divisore += CONST_GREAT_15_COMPLEX
        total_frequency += frequency
        if(len(word)==0):
            frequency_complex = total_frequency / 1
        else:
            frequency_complex = total_frequency/len(words)
    if(divisore==0):
        divisore=1
    len_complex = dividendo/divisore
    if (total_frequency > 500):
        total_complex = (frequency_complex + len_complex)/2
    else:
        text_len_complex = (total_frequency * 100) / 500
        total_complex = (frequency_complex + text_len_complex + len_complex) / 3
    return round(total_complex, 2)

def calculateSingleWordIC(word):
    wordLength= len(word)
    singleIC = (wordLength*100)/8
    if(singleIC>100):
        singleIC=100
    return singleIC



