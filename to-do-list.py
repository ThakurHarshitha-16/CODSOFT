#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ColorfulTodoListApp:
    def __init__(self, master):
        self.master = master
        master.title("To-Do List")
        master.geometry("400x300")

        

        self.tasks = []

        # Placing Entry and Buttons on the canvas using place() method
        self.task_entry = tk.Entry(master, width=40, bd=2, relief=tk.FLAT, font=("Arial", 12))
        self.task_entry.place(x=20, y=20)

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", bd=2, relief=tk.FLAT)
        self.add_button.place(x=20, y=60)

        self.task_listbox = tk.Listbox(master, width=50, font=("Arial", 12), selectbackground="#ADD8E6", selectforeground="black", bd=2, relief=tk.FLAT)
        self.task_listbox.place(x=20, y=100)

        self.complete_button = tk.Button(master, text="Mark as Completed", command=self.mark_as_completed, bg="#FFA500", fg="white", bd=2, relief=tk.FLAT)
        self.complete_button.place(x=20, y=260)

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#FF5733", fg="white", bd=2, relief=tk.FLAT)
        self.delete_button.place(x=180, y=260)

        self.refresh_list()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.refresh_list()
            self.task_entry.delete(0, tk.END)

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def mark_as_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index] += " (Completed)"
            self.refresh_list()
            messagebox.showinfo("Good Job!", "Task marked as completed!")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.refresh_list()

def main():
    root = tk.Tk()
    app = ColorfulTodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




