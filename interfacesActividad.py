from abc import ABC

# Interface
class HeroActions(ABC):
    def __init__(self, hp: float, mana: float, mainAttr: int, name: str) -> None:
        self.hp = hp
        self.mana = mana
        self.mainAttr = mainAttr
        self.name = name

    def attack(self, enemy: str, dmg: float, dmgType: str) -> str:
        # return f'Im attacking {enemy}, doing him {dmg} with {dmgtype}'
        return f'Im attacking {enemy}, doing him {dmg} with {dmgType}. '

    def heal(self, ally: str, amount: float) -> str:
        return f'Im healing {ally} by {amount}. '

# Class 1
class CarryHero(HeroActions):
    def __init__(self, hp: float, mana: float, mainAttr: int, name: str) -> None:
        super().__init__(hp, mana, mainAttr, name)
        
    def attack(self, enemy: str, dmg: float, dmgType: str) -> str:
        return super().attack(enemy, dmg, dmgType) + f'And Im a carry'

    def heal(self, ally: str, amount: float) -> str:
        return super().heal(ally, amount) + f'And Im a carry'

    def __str__(self) -> str:
        return f'My name is {self.name} and my main attribute is {self.mainAttr}'

        # Class 2
class SupportHero(HeroActions):
    def __init__(self, hp: float, mana: float, mainAttr: int, name: str) -> None:
        super().__init__(hp, mana, mainAttr, name)
        
    def attack(self, enemy: str, dmg: float, dmgType: str) -> str:
        return super().attack(enemy, dmg, dmgType) + f'And Im a support'

    def heal(self, ally: str, amount: float) -> str:
        return super().heal(ally, amount) + f'And Im a support'

    def __str__(self) -> str:
        return f'My name is {self.name} and my main attribute is {self.mainAttr}'

cHero1 = CarryHero(600, 230, 'Agility', 'Morphling')
print(cHero1)
print(cHero1.attack('Abaddon', 67.5, 'PhysicalDamage'))
print(cHero1.heal('Clinkz', 200.0))

cHero2 = SupportHero(600, 230, 'Inteligence', 'Dazzle')
print(cHero2)
print(cHero2.attack('Abaddon', 67.5, 'PhysicalDamage'))
print(cHero2.heal('Clinkz', 200.0))