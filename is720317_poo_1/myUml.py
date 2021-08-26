class Programmer:
    
    def __init__(self, name, age, favLang):
        self.name = name
        self.age = age
        self.favLang = favLang
    
    def program(self):
        return f'{self.name} is programming right now'
    
    def debug(self):
        return f'{self.name} is debugging right now'

    def deploy(self, host):
        return f'{self.name} is deploying an app in {host}'

    # Dunder methods
    def __str__(self):
        return f'{self.name} is a {self.age} year old programmer that loves {self.favLang}'

class FrontEndProgrammer(Programmer):

    langUsed = ''

    def __init__(self, name, age, favLang):
        super().__init__(name, age, favLang)

    def __str__(self):
        return f'{self.name} is a frontend developer that uses {self.langUsed} at work'

    def programBE(self, app):
        return f'{self.name} is devoloping the frontend of {self.app}'

    @classmethod
    def changeLangUsed(cls, lang):
        lang = lang.lower()
        if lang in ['javascript', 'html', 'css']:
            cls.lang = lang
        else:
            print('Error. This language is not used in frontend dev.')

class BackEndProgrammer(Programmer):
    
    langUsed = ''

    def __init__(self, name, age, favLang):
        super().__init__(name, age, favLang)

    def __str__(self):
        return f'{self.name} is a backend developer that uses {self.langUsed} at work'

    def programBE(self, app):
        return f'{self.name} is devoloping the backend of {self.app}'

    @classmethod
    def changeLangUsed(cls, lang):
        lang = lang.lower()
        if lang in ['php', 'python', 'nodejs']:
            cls.lang = lang
        else:
            print('Error. This language is not used in backend dev.')

p1 = Programmer('Daniel', 22, 'C')
print(p1.program())
print(p1.deploy('GoDaddy'))

# Uso de __str__
print(p1)

p2 = FrontEndProgrammer('Javier', 21, 'JavaScript')
p2.langUsed = 'React -JS'
print(p2)

p3 = BackEndProgrammer('Andres', 31, 'NodeJs')
p3.langUsed = 'NodeJs'
print(p3)
print(Programmer.p3)