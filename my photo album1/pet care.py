class Pet:
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.__health = health

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
        else:
            print("Health must be between 0 and 100.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.__health}%")


class Dog(Pet):
    def make_sound(self):
        print(f"{self.name} says: Woof! Woof!")


class Cat(Pet):
    def make_sound(self):
        print(f"{self.name} says: Meow!")


class Bird(Pet):
    def make_sound(self):
        print(f"{self.name} says: Tweet! Tweet!")


dog = Dog("Buddy", 3, 90)
cat = Cat("Luna", 2, 85)
bird = Bird("Rio", 1, 95)


print("===== PET CARE DASHBOARD =====")

dog.display_info()
dog.make_sound()

print()

cat.display_info()
cat.make_sound()

print()

bird.display_info()
bird.make_sound()


print("\n===== HEALTH UPDATE =====")

print("Buddy's old health:", dog.get_health())

dog.set_health(95)

print("Buddy's new health:", dog.get_health())


print("\n===== POLYMORPHISM =====")

pets = [dog, cat, bird]

for pet in pets:
    pet.make_sound()