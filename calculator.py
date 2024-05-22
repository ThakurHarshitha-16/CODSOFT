#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = entry_op.get()
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operation"
    
    label_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x300")  


root.configure(bg="#FFFFFF")  

label1 = tk.Label(root, text="Enter first number :",bg='#90EE90')
label1.place(x=20, y=20)

entry1 = tk.Entry(root)
entry1.place(x=200, y=20)

label2 = tk.Label(root, text="Enter second number :",bg='yellow')
label2.place(x=20, y=50)

entry2 = tk.Entry(root)
entry2.place(x=200, y=50)

label_op = tk.Label(root, text="Enter operation (+ , - , * , / ) :",bg='#ADD8E6')
label_op.place(x=20, y=80)

entry_op = tk.Entry(root)
entry_op.place(x=200, y=80)

button = tk.Button(root, text="Calculate", command=calculate,bg='#FFB6C1')
button.place(x=200, y=120)

label_result = tk.Label(root, text="")
label_result.place(x=20, y=150)

root.mainloop()


# In[ ]:





# In[ ]:




