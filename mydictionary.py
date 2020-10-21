

from PyDictionary import PyDictionary

class Mydictionary:
    word=''
    def __init__(self,word):
        
        self.word=word

    def giveMeaning(self):
        dictionary=PyDictionary()
        x=dictionary.meaning(self.word)
        xx=str(x['Noun'][0])
        print(f'meaning: {xx}')
        return (x['Noun'][0])
