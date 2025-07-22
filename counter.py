import tkinter as tk
count=0
def increase():
    global count
    count +=1
    label.config(text=f"Count:{count}")

def reset():
    global count
    count =0
    label.config(text=f"Count:{count}")

def exit():
    root.destroy()

root=tk.Tk()
root.title("Counter")
root.geometry("450x450")    
root.resizable(True,True)
root.configure(bg="gray")

label=tk.Label(root,text='Count:0',font=("Arial",24),bg="#f0f0f0")
label.pack(pady=20)

button=tk.Button(root,text='Click',command=increase,width=10,font=("Arial",24),bg="#f0f0f0")
button.pack(pady=20)

reset_button = tk.Button(root, text="Reset", font=("Arial", 12), width=10, command=reset, bg="#f39c12", fg="white")
reset_button.pack(pady=20)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), width=10, command=exit, bg="#e74c3c", fg="white")
exit_button.pack(pady=20)

root.mainloop()
    
