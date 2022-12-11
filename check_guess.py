from start_game import StartGame

class CheckGuess:
    def __init__(self, user_guess_list, shuffled_word_list):
        self.user_guess_list = user_guess_list
        self.shuffled_word_list = shuffled_word_list

    def check_user_guess(self):
        # does not work, need to sort each word in the list then compare
    #    potential_matches = ''.join(sorted(self.user_guess_list))
    #    potential_shuffled_matches = ''.join(sorted(self.shuffled_word_list))

       for i in range(len(self.user_guess_list)):
            potential_matches = ''.join(sorted(self.user_guess_list[i]))
            potential_shuffled_matches = ''.join(sorted(self.shuffled_word_list[i]))
            
            if potential_matches == potential_shuffled_matches:
                return True
            else:
                return False

# if __name__ == '__main__':
#     input = ["pawn", "king", "queen"]
#     word_list = ["pwn", "nikg", "eueuq"]

#     check_guess = CheckGuess(input, word_list)
#     print(check_guess.check_user_guess())
