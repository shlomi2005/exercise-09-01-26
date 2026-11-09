from classes.Engine import Engine


class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start(self):
        return f"{self.model}: engine {self.engine.hp}hp started"
