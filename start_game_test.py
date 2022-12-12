import unittest

from start_game import StartGame

class StartGameTest(unittest.TestCase):
    word_list = ['apple', 'banana', 'orange', 'pear', 'grape', 'watermelon', 'pineapple', 'strawberry', 'blueberry', 'raspberry']
    
    def setUp(self):
        self.start_game = StartGame(self.word_list)

    def tearDown(self):
        del self.start_game

    def test_object_created(self):
        self.assertEqual(self.start_game.word_list, self.word_list)

    def test_object_not_created(self):
        with self.assertRaises(ValueError):
            start_game = StartGame('')

    def test_invalid_object(self):
        with self.assertRaises(ValueError):
            start_game = StartGame('')
            start_game.shuffle_words()

    def test_word_shuffle(self):
        self.assertNotEqual(self.start_game.shuffled_word_list, self.word_list)

if __name__ == '__main__':
    unittest.main()

