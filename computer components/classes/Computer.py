class Computer:
    def __init__(self, cpu, ram, disk):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    def __str__(self):
        return f"{self.cpu.cores}-core, {self.cpu.gHz}GHz, {self.ram.gb_r}GB RAM, {self.disk.gb_s}GB SSD "

    def can_run(self, mini_core, mini_gb):
        if mini_core >= self.cpu.cores:
            return False
        if mini_gb >= self.ram.gb_r:
            return False
        return True
