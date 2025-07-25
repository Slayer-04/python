import tkinter as tk

root = tk.Tk()
root.title("To-Do List")
root.geometry("450x500")
root.resizable(True, True)
root.configure(bg="gray")

tasks = []  # List to store tuples of (frame, var)

def Add():
    task_text = entry.get().strip()
    if not task_text:
        return  # Ignore empty input

    task_frame = tk.Frame(root, bg="gray")
    task_frame.pack(anchor="w", padx=20, pady=5)

    var = tk.IntVar()
    check = tk.Checkbutton(task_frame, text=task_text, variable=var,
                           font=("Arial", 18), bg="gray", anchor="w")
    check.pack(side="left")

    # Save task info for deletion later
    tasks.append((task_frame, var))

    entry.delete(0, tk.END)

def DeleteCompleted():
    # Iterate over a copy of the list because we will modify it
    for task_frame, var in tasks[:]:
        if var.get() == 1:  # Checked
            task_frame.destroy()
            tasks.remove((task_frame, var))

# GUI widgets
label = tk.Label(root, text='Enter the to-do item:', width=20, font=("Arial", 20), bg="white")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 18), width=25)
entry.pack(pady=10)

button_add = tk.Button(root, text='Add Task', command=Add, width=12, font=("Arial", 20), bg="#f0f0f0")
button_add.pack(pady=10)

button_delete = tk.Button(root, text='Delete Completed', command=DeleteCompleted,
                          width=16, font=("Arial", 18), bg="#ff9999")
button_delete.pack(pady=10)

root.mainloop()
