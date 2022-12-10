import unittest

from check_guess import CheckGuess

class TestCheckGuess(unittest.TestCase):
    user_guess_list = [['cda', 'btrf', 'cfr'], ['dcd', 'ete', 'fgsefg']]
    shuffled_word_list = [['dca', 'tbfr', 'crf'], ['cdd', 'tee', 'gsfefg']]

    def test_object_created(self):
        check_guess = CheckGuess(self.user_guess_list, self.shuffled_word_list)
        assert check_guess.user_guess_list == self.user_guess_list
        assert check_guess.shuffled_word_list == self.shuffled_word_list

    def test_check_user_guess(self):
        check_guess = CheckGuess(self.user_guess_list, self.shuffled_word_list)
        assert check_guess.check_user_guess() == True

if __name__ == '__main__':
    unittest.main()