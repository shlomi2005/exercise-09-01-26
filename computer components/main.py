from classes.Computer import Computer
from classes.CPU import CPU
from classes.RAM import RAM
from classes.Disk import Disk


pc = Computer(CPU(8, 3.2), RAM(8), Disk(512))
print(pc)
print("Can run the game?", pc.can_run(6, 16))
print("Can run the game?", pc.can_run(6, 4))
