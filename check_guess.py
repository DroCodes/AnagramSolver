from start_game import StartGame

class CheckGuess:
    def __init__(self, user_guess_list, shuffled_word_list):
        if user_guess_list == '' or shuffled_word_list == '':
            raise ValueError('user_guess_list and shuffled_word_list cannot be empty')
        self.user_guess_list = user_guess_list
        self.shuffled_word_list = shuffled_word_list

    def check_user_guess(self):
        """Checks user guess against shuffled word list"""
        match = 0
        for i in range(len(self.user_guess_list)):
            potential_matches = ''.join(sorted(self.user_guess_list[i].lower()))
            shuffled_words = ''.join(sorted(self.shuffled_word_list[i]))

            if potential_matches == '':
                raise ValueError('user_guess_list cannot be empty')

            if potential_matches == shuffled_words:
                match += 1
                if match == len(self.user_guess_list):
                    return True
            else:
                return False