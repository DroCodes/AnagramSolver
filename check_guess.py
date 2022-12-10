from start_game import StartGame

class CheckGuess:
    def __init__(self, user_guess_list, shuffled_word_list):
        self.user_guess_list = user_guess_list
        self.shuffled_word_list = shuffled_word_list

    def check_user_guess(self):
        for i in range(len(self.user_guess_list)):
            if self.user_guess_list[i].sort() == self.shuffled_word_list[i].sort():
                return True
            else:
                return False