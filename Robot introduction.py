class Robot:

    def __init__(self, name, color, job):
        self.name = name
        self.color = color
        self.job = job

    def introduce(self):
        print("Hello! My name is", self.name)
        print("My color is", self.color)
        print("My job is", self.job)

    def move(self):
        print(self.name, "is moving!")

    def talk(self):
        print(self.name, "says: Hello, nice to meet you!")


robot1 = Robot("Robo", "Blue", "Helping people")

print("=== Robot Introduction ===\n")

robot1.introduce()
robot1.move()
robot1.talk()