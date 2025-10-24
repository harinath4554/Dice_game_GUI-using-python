import tkinter as tk
import random

root = tk.Tk()
root.title("Dice Game")
root.geometry("800x600")

dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

label_player_1 = tk.Label(root, text="", font=("Times New Roman", 40))
label_player_1.pack(pady=10)

label_player_2 = tk.Label(root, text="", font=("Times New Roman", 40))
label_player_2.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman", 40))
result_label.pack(pady=20)

sum_p1 = None
sum_p2 = None
turn = 1  

def roll():
    global sum_p1, sum_p2, turn

    if turn == 1:
        roll1 = random.choice(dice)
        roll2 = random.choice(dice)
        sum_p1 = dice.index(roll1) + 1 + dice.index(roll2) + 1
        label_player_1.config(text=f"Player 1: {roll1} {roll2} (Sum: {sum_p1})")
        turn = 2  
        result_label.config(text="Player 2's turn", fg="black")

    elif turn == 2:
        roll3 = random.choice(dice)
        roll4 = random.choice(dice)
        sum_p2 = dice.index(roll3) + 1 + dice.index(roll4) + 1
        label_player_2.config(text=f"Player 2: {roll3} {roll4} (Sum: {sum_p2})")
        show_result()

def show_result():
    global sum_p1, sum_p2, turn

    if sum_p1 > sum_p2:
        result_label.config(text="🏆 Player 1 Wins!", fg="green")
    elif sum_p2 > sum_p1:
        result_label.config(text="🏆 Player 2 Wins!", fg="orange")
    else:
        result_label.config(text="🤝 It's a Tie!", fg="blue")

    root.after(4000, reset_game)  

def reset_game():
    global sum_p1, sum_p2, turn
    sum_p1 = None
    sum_p2 = None
    turn = 1
    label_player_1.config(text="")
    label_player_2.config(text="")
    result_label.config(text="Player 1's turn", fg="black")

roll_button = tk.Button(root, text="Roll Dice", font=("Times New Roman", 20),
                        width=30, bg="#EB9CF7", fg="red", bd=2, command=roll)
roll_button.pack(pady=20)

reset_game()
root.mainloop()
