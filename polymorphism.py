# Poly-morphism
# Poly = many
# Morphism = form  "Many Forms"

class Language:
    def say_hello(self):
        raise NotImplementedError('Please use say_hello class in child class')

class French(Language):
    def say_hello(self):
        print('Bonjour')


class Chinese(Language):
    def say_hello(self):
        print('Nihao')


def intro(lang):
    lang.say_hello()


sarthak = French()
john = Chinese()

intro(sarthak)
intro(john)
