import tkinter as tk

def on_button_click():
  label["text"] = "Baf"

root = tk.Tk()
root.geometry("1000x800+100+100")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(padx=5, pady=50)
label = tk.Label(font=("Inter", 50, "bold"))
label.pack(padx=5, pady=100)
root.mainloop()   