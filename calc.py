import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Mainframe")
root.geometry("500x500")
root.minsize(200, 200)

font_general = font.Font(size=20, family="Arial")
last_result = None

entry = tk.Entry(root, font=font_general, borderwidth=20, justify='right')
entry.grid(row=0, column=0, columnspan=4)


def add_char(char):
	global last_result
	if entry.get() == str(last_result):
		clear_entry()
	entry.insert(len(entry.get()), char)


def clear_entry():
	entry.delete(0, tk.END)


def show_result():
	global last_result
	try:
		result = eval(entry.get(), {"__builtins__": None}, {})
		last_result = result
		entry.delete(0, tk.END)
		entry.insert(0, str(result))
	except Exception:
		entry.delete(0, tk.END)
		entry.insert(0, "Error")


button1 = tk.Button(root, text="1", font=font_general, command=lambda: add_char("1"))
button2 = tk.Button(root, text="2", font=font_general, command=lambda: add_char("2"))
button3 = tk.Button(root, text="3", font=font_general, command=lambda: add_char("3"))
button4 = tk.Button(root, text="4", font=font_general, command=lambda: add_char("4"))
button5 = tk.Button(root, text="5", font=font_general, command=lambda: add_char("5"))
button6 = tk.Button(root, text="6", font=font_general, command=lambda: add_char("6"))
button7 = tk.Button(root, text="7", font=font_general, command=lambda: add_char("7"))
button8 = tk.Button(root, text="8", font=font_general, command=lambda: add_char("8"))
button9 = tk.Button(root, text="9", font=font_general, command=lambda: add_char("9"))
button0 = tk.Button(root, text="0", font=font_general, command=lambda: add_char("0"))

button_add = tk.Button(root, text="+", font=font_general, command=lambda: add_char("+"))
button_sub = tk.Button(root, text="-", font=font_general, command=lambda: add_char("-"))
button_mul = tk.Button(root, text="*", font=font_general, command=lambda: add_char("*"))
button_div = tk.Button(root, text="/", font=font_general, command=lambda: add_char("/"))

button_res = tk.Button(root, text="=", font=font_general, command=show_result)
button_clr = tk.Button(root, text="Clear", font=font_general, command=lambda: entry.delete(0, tk.END))

button7.grid(row=1, column=0, sticky="nsew")
button8.grid(row=1, column=1, sticky="nsew")
button9.grid(row=1, column=2, sticky="nsew")

button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")

button1.grid(row=3, column=0, sticky="nsew")
button2.grid(row=3, column=1, sticky="nsew")
button3.grid(row=3, column=2, sticky="nsew")

button_mul.grid(row=4, column=0, sticky="nsew")
button0.grid(row=4, column=1, sticky="nsew")
button_div.grid(row=4, column=2, sticky="nsew")

button_clr.grid(row=1, column=3, sticky="nsew")
button_sub.grid(row=2, column=3, sticky="nsew")
button_add.grid(row=3, column=3, sticky="nsew")
button_res.grid(row=4, column=3, sticky="nsew")

for column in range(4):
	root.grid_columnconfigure(column, weight=1)

for row in range(5):
	root.grid_rowconfigure(row, weight=1)

root.mainloop()