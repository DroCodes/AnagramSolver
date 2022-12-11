from check_guess import CheckGuess
from start_game import StartGame

import tkinter
# TODO - clean up ui, add more words and have the words randomly selected

possible_words = ['king', 'aardvark', 'trailer', 'python', 'computer', 'science', 'programming', 'mathematics', 'player', 'condition']

initialize_game = StartGame(possible_words)

def replay():
    initialize_game = StartGame(possible_words)
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
    user_guess = [user_input1.get(), user_input2.get(), user_input3.get(), user_input4.get(), user_input5.get(), user_input6.get(), user_input7.get(), user_input8.get(), user_input9.get(), user_input10.get()]

    check_guess = CheckGuess(user_guess, initialize_game.shuffled_word_list)

    if check_guess.check_user_guess():
        create_popup("You Win!")
        replay()
    else:
        create_popup("You Lose!")
        replay()

def create_popup(msg):
    """Creates a popup window when the user wins"""
    popup = tkinter.Tk()
    popup.wm_title(msg)
    label = tkinter.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = tkinter.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()

main = tkinter.Tk()
main.title("Word Scramble!")
main.geometry("750x750")

label1 = tkinter.Label(main, text=initialize_game.shuffled_word_list[0])
label1.grid(row=0, column=0, columnspan=6)

label2 = tkinter.Label(main, text=initialize_game.shuffled_word_list[1])
label2.grid(row=1, column=0, columnspan=6)

label3 = tkinter.Label(main, text=initialize_game.shuffled_word_list[2])
label3.grid(row=2, column=0, columnspan=6)

label4 = tkinter.Label(main, text=initialize_game.shuffled_word_list[3])
label4.grid(row=3, column=0, columnspan=6)

label5 = tkinter.Label(main, text=initialize_game.shuffled_word_list[4])
label5.grid(row=4, column=0, columnspan=6)

label6 = tkinter.Label(main, text=initialize_game.shuffled_word_list[5])
label6.grid(row=5, column=0, columnspan=6)

label7 = tkinter.Label(main, text=initialize_game.shuffled_word_list[6])
label7.grid(row=6, column=0, columnspan=6)

label8 = tkinter.Label(main, text=initialize_game.shuffled_word_list[7])
label8.grid(row=7, column=0, columnspan=6)

label9 = tkinter.Label(main, text=initialize_game.shuffled_word_list[8])
label9.grid(row=8, column=0, columnspan=6)

label10 = tkinter.Label(main, text=initialize_game.shuffled_word_list[9])
label10.grid(row=9, column=0, columnspan=6)

# user input
user_input1 = tkinter.Entry(main)
user_input1.grid(row=0, column=7, columnspan=6)

user_input2 = tkinter.Entry(main)
user_input2.grid(row=1, column=7, columnspan=6)

user_input3 = tkinter.Entry(main)
user_input3.grid(row=2, column=7, columnspan=6)

user_input4 = tkinter.Entry(main)
user_input4.grid(row=3, column=7, columnspan=6)

user_input5 = tkinter.Entry(main)
user_input5.grid(row=4, column=7, columnspan=6)

user_input6 = tkinter.Entry(main)
user_input6.grid(row=5, column=7, columnspan=6)

user_input7 = tkinter.Entry(main)
user_input7.grid(row=6, column=7, columnspan=6)

user_input8 = tkinter.Entry(main)
user_input8.grid(row=7, column=7, columnspan=6)

user_input9 = tkinter.Entry(main)
user_input9.grid(row=8, column=7, columnspan=6)

user_input10 = tkinter.Entry(main)
user_input10.grid(row=9, column=7, columnspan=6)

# start game button
start_game_button = tkinter.Button(main, text="Start Game", command=replay)
start_game_button.grid(row=10, column=0, columnspan=6)

# check guess button
check_guess_button = tkinter.Button(main, text="Check Guess", command=submit_guess)
check_guess_button.grid(row=10, column=7, columnspan=6)

# quit button
quit_button = tkinter.Button(main, text="Quit", command=main.destroy)
quit_button.grid(row=11, column=0, columnspan=6)

main.mainloop()
