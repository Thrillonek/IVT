import tkinter as tk

def on_button_click(color):
  root.configure(background=color)

root = tk.Tk()
root.geometry("1000x800+100+100")

button1 = tk.Button(root, text="Modrá", command=lambda: on_button_click("blue"))
button1.pack(padx=20, pady=0, side="left")
button2 = tk.Button(root, text="Červená", command=lambda: on_button_click("red"))
button2.pack(padx=20, pady=0, side="left")
button3 = tk.Button(root, text="Zelená", command=lambda: on_button_click("green"))
button3.pack(padx=20, pady=0, side="left")
root.mainloop()   