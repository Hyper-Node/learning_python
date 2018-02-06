class Test(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    @property
    def c(self):
        return self.a + self.b

class Listentest(object):
    def __init__(self,meine_liste):
        self.meine_liste = meine_liste

    @property
    def mein_text(self):
        mein_text = ""

        for element in self.meine_liste:
            mein_text += str(element.char)

        return mein_text




class ListenElement(object):
    def __init__(self,character, confidence):
        self.char = character
        self.confidence = confidence


# erster Test
first_test = Test(1,2)
print(first_test.c)

first_test.a = 4
print(first_test.c)


#zweiter Test
meine_liste = [ListenElement('a',99),ListenElement('b',98),ListenElement('c',92)]
listen_test = Listentest(meine_liste)
print(listen_test.mein_text)
listen_test.meine_liste.append(ListenElement('d',12))
print(listen_test.mein_text)

