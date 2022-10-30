import tkinter as tk


FONT = "Arial"

root = tk.Tk()

root.geometry("500x500")
root.title("Message Compiler")

lbl = tk.Label(root, text="Hello World!", font=(FONT, 18))
lbl.pack(padx=20, pady=20)

tb = tk.Text(root, height=3, font=(FONT, 16))
tb.pack(padx=10, pady=10)

input = tk.Entry(root)
input.pack()

btn = tk.Button(root, text="Enter", font=(FONT, 18))
btn.pack(padx=10, pady=10)

btnfr = tk.Frame(root)
btnfr.columnconfigure(0, weight=1)
btnfr.columnconfigure(1, weight=1)
btnfr.columnconfigure(2, weight=1)

btn1 = tk.Button(btnfr, text="1", font=(FONT, 18))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
btn1 = tk.Button(btnfr, text="2", font=(FONT, 18))
btn1.grid(row=0, column=1, sticky=tk.W + tk.E)
btn1 = tk.Button(btnfr, text="3", font=(FONT, 18))
btn1.grid(row=0, column=2, sticky=tk.W + tk.E)

btn1 = tk.Button(btnfr, text="4", font=(FONT, 18))
btn1.grid(row=1, column=0, sticky=tk.W + tk.E)
btn1 = tk.Button(btnfr, text="5", font=(FONT, 18))
btn1.grid(row=1, column=1, sticky=tk.W + tk.E)
btn1 = tk.Button(btnfr, text="6", font=(FONT, 18))
btn1.grid(row=1, column=2, sticky=tk.W + tk.E)


btnfr.pack(fill="x")


root.mainloop()
