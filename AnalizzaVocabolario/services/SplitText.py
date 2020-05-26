def tokenize(text):
    """QUESTO METODO CI SERVE PER TOKENIZZARE E PULIRE IL TESTO"""
    lettere = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZàèéòùìÀÈÌÒÙ '
    words = dict()
    for x in text:
        if x not in lettere:
            text = text.replace(x, "")
    tokens = [t.lower() for t in text.split()]
    tokens.sort()
    for t in tokens:
        if words.get(t, 'None') == 'None':
            x = tokens.count(t)
            words.update({t: x})
    return words