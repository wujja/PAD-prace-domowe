class Game():
    def _play(self):
        self.how_many_players()          
        print("Gra się rozpoczeła, liczba graczy {}".format(self.no_players))

    def how_many_players(self):
        no_players = None
        while (no_players is not type(int) and no_players not in range(1,3)):           
            try:
                no_players = int(input("How many players?\n"))
                if(no_players not in range(1,3)):
                    print("Number must 1 or 2")
                else:
                    self.no_players = no_players
            except:
                print("Please write a number")

class Hangman(Game):
    def __init__(self):
        self.level = ""
        self.level_of_difficulty = ["beginner", "intermediate", "advanced"]
        self.list_of_words = ["apple", "orange", "car", "cat", "cow", "pineapple", "window", "pensil"]

    def difficult_level(self):
        level = ""
        list_of_choise = ["a", "b", "i"]
        while(level not in list_of_choise):
            try:
                level = input("Which level of difficulty do you want to play? Type b - beginner, i - intermediate, a - advanced:\n" )
                if(level not in list_of_choise):
                    print("Please write a, b or i")
            except:
                print("Something goes wrong") #chyba niepotrzebne
        self.how_many_tries(level)

    def how_many_tries(self, level_from_user = ""):
        if(level_from_user == "b" or self.level == self.level_of_difficulty[0]):
            self.level = self.level_of_difficulty[0]
            self.no_tries = 8
        elif(level_from_user == "i" or self.level == self.level_of_difficulty[1]):
            self.level = self.level_of_difficulty[1]
            self.no_tries = 5
        elif(level_from_user == "a" or self.level == self.level_of_difficulty[2]):
            self.level = self.level_of_difficulty[2]
            self.no_tries = 3


    def update_information(self):
        print(f'Your word looks now: {self.word.word_to_show}')
        print(f'Left tries: {self.no_tries}')
    
    def _play(self):
        self.game_over = False
        self.round = 1
        super()._play()
        self.difficult_level()
        print(f'Difficulty level: {self.level}, number of tries {self.no_tries}')
        self.choose_word()
        print(self.word.word_to_show)
        self.next_round()

        
    
    def end_of_game(self):
        if(self.word.word == self.word.word_to_show):
            print("You won congratulation!!")
            print(f'Word to guess: {self.word.word_to_show}')
            self.game_over = True
        if(self.no_players == 1 and self.no_tries == 0):
            self.game_over = True
        elif(self.no_players != 1 and self.no_tries == 0):
            if(self.round != self.no_players):
                self.round += 1
                self.how_many_tries()
                print(f'Round {self.round}')
                self.choose_word()
            else:
                self.game_over = True

    
    def choose_word(self):
        import random
        if (self.no_players == 1):
            self.word = WordToGuess(random.choice(self.list_of_words))
        else:
            word = ""
            while(not word.isalpha()):
                word = input("Please write a word for other player: \n")
                self.word = WordToGuess(word.lower())  

    def next_round(self):
        letter = ""
        while(len(letter) != 1 and not letter.isalpha()):
            letter = input("Please type a letter: ")
            if(len(letter) == 1 and not letter.isalpha()):
                print("It's not one letter")
        
        if(not self.word.new_letter(letter=letter.lower())):
            self.no_tries -= 1
        self.end_of_game()

        if(self.game_over):
            once_again = input("Do you want to play once again? Type 'y' to play once again:\n")
            if(once_again.lower()== 'y'):
                self._play()
        else:
            self.update_information()
            self.next_round()
            
        
class WordToGuess():
    
    def __init__(self, word):
        self.word = word
        self.changeToFloor()
    
    def changeToFloor(self):
        self.word_to_show = '_' * len(self.word)

    def new_letter(self, letter):
        if (self.word.count(letter) > 0):
            my_list = [i for i, j in enumerate(self.word) if j==letter]
            word_as_list = list(self.word_to_show)
            for i in range(len(self.word)):
                if(i in my_list):
                    word_as_list[i] = letter
            self.word_to_show = "".join(word_as_list)
            print("Good choice")
            print(f'Your current state: {self.word_to_show}')
            return True
        else:
            print("Bad choice")
            return False



d = Hangman()
d._play()