class Task:
    def __init__(self, name):
        self.name = name


class Pyke:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))
