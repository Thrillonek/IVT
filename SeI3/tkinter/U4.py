import tkinter as tk
from PIL import Image, ImageTk

def on_button_click():
  text = btn["text"]
  if text == "OFF":
    root.configure(background="black")
    btn["text"] = "ON"
  else:
    root.configure(background="white")
    btn["text"] = "OFF"

root = tk.Tk()
root.geometry("1000x800+100+100")

image = Image.open("./SeI3/tkinter/image.png")
photo = ImageTk.PhotoImage(image)

btn = tk.Button(root, text="OFF", command=on_button_click, image=photo)
btn.pack(padx=20, pady=20)
root.mainloop()   