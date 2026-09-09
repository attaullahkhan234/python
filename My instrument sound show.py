from abc import ABC, abstractmethod


class Instrument(ABC):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display(self):
        print(f"Instrument: {self.name}, Type: {self.type}")

    @abstractmethod
    def play_sound(self):
        pass


class Guitar(Instrument):
    def __init__(self, name, type, strings):
        super().__init__(name, type)
        self.strings = strings

    def play_sound(self):
        print(f"{self.name} ({self.strings} strings) plays: Strum! Strum!")


class Piano(Instrument):
    def __init__(self, name, type, keys):
        super().__init__(name, type)
        self.keys = keys

    def play_sound(self):
        print(f"{self.name} ({self.keys} keys) plays: Plink! Plink!")


class Drums(Instrument):
    def __init__(self, name, type, pieces):
        super().__init__(name, type)
        self.pieces = pieces

    def play_sound(self):
        print(f"{self.name} ({self.pieces} pieces) plays: Boom! Boom!")


guitar = Guitar("Acoustic Guitar", "String", 6)
piano = Piano("Grand Piano", "Keyboard", 88)
drums = Drums("Drum Set", "Percussion", 5)


print("=== Music Instrument Sound Show ===\n")

for instrument in [guitar, piano, drums]:
    instrument.display()
    instrument.play_sound()
    print()