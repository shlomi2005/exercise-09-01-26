from classes.Character import Character
from classes.Mage import Mage
from classes.Warrior import Warrior


def attack(attacker, defender):
    defender.life -= attacker.attack_power()
    print(f"{attacker.name}hits {defender.name} for {attacker.attack_power()}")


conan = Warrior("Conan", 100)
merlin = Mage("Merlin", 60)
attack(conan, merlin)
attack(merlin, conan)
print(merlin.name, merlin.life)
print(conan.name, conan.life)
