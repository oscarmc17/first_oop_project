# Poly-morphism
# Poly = many
# Morphism = form  "Many Forms"

class French:
    def say_hello(self):
        print('Bonjour')


class Chinese:
    def say_hello(self):
        print('Nihao')


def intro(lang):
    lang.say_hello()


sarthak = French()
john = Chinese()

intro(sarthak)
intro(john)
