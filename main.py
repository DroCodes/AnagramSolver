import random
from check_guess import CheckGuess
from start_game import StartGame

import tkinter

def select_words():
    """Selects words from the possible_words list and returns a list of 10 words"""
    word_file = open("words.txt", "r")
    possible_words = word_file.read().splitlines()
    word_file.close()
    selected_words = random.sample(possible_words, 10)

    return selected_words

try:
    initialize_game = StartGame(select_words())
except ValueError:
    print('word_list cannot be empty')

def replay():
    """Resets the game"""
    initialize_game = StartGame(select_words())
    # reset labels
    label1.config(text=initialize_game.shuffled_word_list[0])
    label2.config(text=initialize_game.shuffled_word_list[1])
    label3.config(text=initialize_game.shuffled_word_list[2])
    label4.config(text=initialize_game.shuffled_word_list[3])
    label5.config(text=initialize_game.shuffled_word_list[4])
    label6.config(text=initialize_game.shuffled_word_list[5])
    label7.config(text=initialize_game.shuffled_word_list[6])
    label8.config(text=initialize_game.shuffled_word_list[7])
    label9.config(text=initialize_game.shuffled_word_list[8])
    label10.config(text=initialize_game.shuffled_word_list[9])

    # reset inputs
    user_input1.delete(0, 'end')
    user_input2.delete(0, 'end')
    user_input3.delete(0, 'end')
    user_input4.delete(0, 'end')
    user_input5.delete(0, 'end')
    user_input6.delete(0, 'end')
    user_input7.delete(0, 'end')
    user_input8.delete(0, 'end')
    user_input9.delete(0, 'end')
    user_input10.delete(0, 'end')

def submit_guess():
    """Submits the user's guess and checks if it is correct"""
    user_guess = [user_input1.get(), user_input2.get(), user_input3.get(), user_input4.get(), user_input5.get(), user_input6.get(), user_input7.get(), user_input8.get(), user_input9.get(), user_input10.get()]

    try:
        check_guess = CheckGuess(user_guess, initialize_game.shuffled_word_list)
    except ValueError as err:
        print(err)

    try:
        if check_guess.check_user_guess():
            create_popup("You Win!")
            replay()
        else:
            create_popup("You Lose!")
            replay()
    except ValueError as err:
        print(err)

def create_popup(msg):
    """Creates a popup window when the user wins"""
    popup = tkinter.Tk()
    popup.wm_title(msg)
    popup.geometry("%dx%d+%d+%d" % (200, 100, x, y))

    label = tkinter.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

main = tkinter.Tk()
main.title("Word Scramble!")
main.geometry("600x600")

# gets screen dimensions
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# center the window
x = (screen_width/2) - (600/2)
y = (screen_height/2) - (600/2)
main.geometry("%dx%d+%d+%d" % (600, 600, x, y))

# start game button
start_game_button = tkinter.Button(main, width=80, padx="10", text="Start Game", command=replay)
start_game_button.grid(row=0, column=0, columnspan=10)

# labels
label1 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[0])
label1.grid(row=1, column=0, columnspan=5)

label2 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[1])
label2.grid(row=2, column=0, columnspan=5)

label3 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[2])
label3.grid(row=3, column=0, columnspan=5)

label4 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[3])
label4.grid(row=4, column=0, columnspan=5)

label5 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[4])
label5.grid(row=5, column=0, columnspan=5)

label6 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[5])
label6.grid(row=6, column=0, columnspan=5)

label7 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[6])
label7.grid(row=7, column=0, columnspan=5)

label8 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[7])
label8.grid(row=8, column=0, columnspan=5)

label9 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[8])
label9.grid(row=9, column=0, columnspan=5)

label10 = tkinter.Label(main, width=40, pady=10, text=initialize_game.shuffled_word_list[9])
label10.grid(row=10, column=0, columnspan=5)

# user input
user_input1 = tkinter.Entry(main)
user_input1.grid(row=1, column=7, columnspan=6)

user_input2 = tkinter.Entry(main)
user_input2.grid(row=2, column=7, columnspan=6)

user_input3 = tkinter.Entry(main)
user_input3.grid(row=3, column=7, columnspan=6)

user_input4 = tkinter.Entry(main)
user_input4.grid(row=4, column=7, columnspan=6)

user_input5 = tkinter.Entry(main)
user_input5.grid(row=5, column=7, columnspan=6)

user_input6 = tkinter.Entry(main)
user_input6.grid(row=6, column=7, columnspan=6)

user_input7 = tkinter.Entry(main)
user_input7.grid(row=7, column=7, columnspan=6)

user_input8 = tkinter.Entry(main)
user_input8.grid(row=8, column=7, columnspan=6)

user_input9 = tkinter.Entry(main)
user_input9.grid(row=9, column=7, columnspan=6)

user_input10 = tkinter.Entry(main)
user_input10.grid(row=10, column=7, columnspan=6)

# check guess button
check_guess_button = tkinter.Button(main, width=20, bg="#90EE90", text="Check Guess", command=submit_guess)
check_guess_button.grid(row=11, column=0, columnspan=5)

# quit button
quit_button = tkinter.Button(main, text="Quit", width=20, bg="red", command=main.destroy)
quit_button.grid(row=11, column=7, columnspan=5)

main.mainloop()
