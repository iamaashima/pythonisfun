from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Entry box
e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def button_equal(event=None):
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(result))
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("+", 4, 1), ("Clear", 4, 2), ("=", 4, 3),
    ("Enter", 5, 0, 4)  # Span across all columns
]

for item in buttons:
    text = item[0]
    row = item[1]
    col = item[2]
    colspan = item[3] if len(item) == 4 else 1
    if text == "Clear":
        btn = Button(root, text=text, width=10, height=2, command=button_clear)
    elif text in ("=", "Enter"):
        btn = Button(root, text=text, width=10 * colspan, height=2, command=button_equal)
    else:
        btn = Button(root, text=text, width=10, height=2, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2)

# Bind Enter key
root.bind('<Return>', button_equal)

root.mainloop()
