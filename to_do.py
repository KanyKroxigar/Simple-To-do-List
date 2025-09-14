import tkinter as tk
from tkinter import messagebox


def add_task():

    task = entry_task.get()
    if task:
  
        listbox_tasks.insert(tk.END, task)
   
        entry_task.delete(0, tk.END)
    else:
     
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():

    try:

        selected_task_index = listbox_tasks.curselection()[0]
    
        listbox_tasks.delete(selected_task_index)
    except IndexError:
       
        messagebox.showwarning("Warning", "You must select a task to delete.")

def mark_task_complete():
  
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        
        current_bg = listbox_tasks.itemcget(selected_task_index, "bg")
        
        if current_bg == "#d3ffd3": 
        
            listbox_tasks.itemconfig(selected_task_index, {'bg':'#ffffff'}) # White
        else:
           
            listbox_tasks.itemconfig(selected_task_index, {'bg':'#d3ffd3'}) # Light green
            
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark.")


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg="#f0f0f0") 


frame_main = tk.Frame(root, bg="#f0f0f0")
frame_main.pack(pady=10, padx=10, fill="both", expand=True)


frame_tasks = tk.Frame(frame_main)
frame_tasks.pack(fill="x", pady=5)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=50, bd=1, font=("Helvetica", 12), selectbackground="#a6a6a6")
listbox_tasks.pack(side=tk.LEFT, fill="both", expand=True)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill="y")

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(frame_main, width=40, font=("Helvetica", 12), bd=1)
entry_task.pack(pady=10)

frame_buttons = tk.Frame(frame_main, bg="#f0f0f0")
frame_buttons.pack(pady=5)

button_add_task = tk.Button(frame_buttons, text="Add Task", width=12, command=add_task, bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"))
button_add_task.pack(side=tk.LEFT, padx=5)

button_delete_task = tk.Button(frame_buttons, text="Delete Task", width=12, command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 10, "bold"))
button_delete_task.pack(side=tk.LEFT, padx=5)

button_mark_task = tk.Button(frame_buttons, text="Mark Complete", width=15, command=mark_task_complete, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold"))
button_mark_task.pack(side=tk.LEFT, padx=5)


root.mainloop()
