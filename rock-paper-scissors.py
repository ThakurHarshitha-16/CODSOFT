#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    result_label.config(text=f"User's choice: {user_choice}\nComputer's choice: {computer_choice}")
    
    if user_choice == computer_choice:
        result_label.config(text=result_label.cget("text") + "\nIt's a tie!", fg="orange")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result_label.config(text=result_label.cget("text") + "\nYou win!", fg="green")
    else:
        result_label.config(text=result_label.cget("text") + "\nYou lose!", fg="red")

def play_again():
    result_label.config(text="")
    user_choice.set("")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")



# Set the window size and position it in the center
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

user_choice = tk.StringVar()

choices_frame = tk.Frame(root, bg="#ffcc00") 
choices_frame.pack(pady=20)

rock_button = tk.Button(choices_frame, text="Rock", bg="#ff6666", command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(choices_frame, text="Paper", bg="#66ccff", command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(choices_frame, text="Scissors", bg="#99ff99", command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white") 
result_label.pack(pady=20)

play_again_button = tk.Button(root, text="Play Again", bg="#ff6666", command=play_again)
play_again_button.pack()

root.mainloop()


# In[ ]:





# In[ ]:




