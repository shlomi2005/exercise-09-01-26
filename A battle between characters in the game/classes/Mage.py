from classes.Character import Character


class Mage(Character):
    def attack_power(self):
        if self.life > 50:
            return 20
        else:
            return 10
