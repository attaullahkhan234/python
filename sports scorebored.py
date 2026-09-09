class criket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Criket  - player: {self.__player}, score: {self.__score}")   

    def play(self):
        print(f"{self.__player} hits a six!")

    def get_score(self):
        return self.__score

    def set_score(self, new__score):
        if new__score >= 0:
            self.__score = new__score
            print(f"Score updated to: {self.__score}")
        else:
            print("Score cannot be negative.")



class football:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football  - player: {self.__player}, score: {self.__score}")   

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score

    def set_score(self, new__score):
        if new__score >= 0:
            self.__score = new__score
            print(f"Score updated to: {self.__score}")
        else:
            print("Score cannot be negative.")


criket = criket("Babar azam", 100)
football = football("Ronaldo", 7)


print("=== Sports Scoreboard ===\n")
for sport in [criket, football]:
    sport.info()
    sport.play()



print("--- Direct change attempt ---")
criket.__score =999
print(f"get score() still shows: {criket.get_score()}")  


print("\n--- updating score ---")
criket.set_score(100)
football.set_score(10)