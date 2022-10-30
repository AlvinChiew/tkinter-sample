from re import L
import tkinter as tk
from tkinter import messagebox


class Program:
    def __init__(self):
        FONT = "Arial"
        FONT_SIZE_BIG = 18
        FONT_SIZE_SMALL = 16
        PADX, PADY = 10, 10

        self.root = tk.Tk()
        self.root.title("Message")

        self.menubar = tk.Menu(self.root)

        self.mnfile = tk.Menu(self.menubar, tearoff=0)
        self.mnfile.add_command(label="Close", command=self.on_closing)
        self.mnfile.add_separator()
        self.mnfile.add_command(label="Close Now", command=exit)

        self.mnaction = tk.Menu(self.menubar, tearoff=0)
        self.mnaction.add_command(label="Show Message", command=self.show_message)

        self.menubar.add_cascade(menu=self.mnfile, label="File")
        self.menubar.add_cascade(menu=self.mnaction, label="Action")
        self.root.config(menu=self.menubar)

        self.lbl = tk.Label(self.root, text="Message", font=(FONT, FONT_SIZE_BIG))
        self.lbl.pack(padx=PADX, pady=PADY)

        self.tb = tk.Text(self.root, height=5, font=(FONT, FONT_SIZE_SMALL))
        self.tb.bind("<KeyPress>", self.shortcut)
        self.tb.pack(padx=PADX, pady=PADY)

        self.checkbtn_state = tk.IntVar()
        self.checkbtn = tk.Checkbutton(
            self.root,
            text="Show Message Box",
            font=(FONT, FONT_SIZE_SMALL),
            variable=self.checkbtn_state,
        )
        self.checkbtn.pack(padx=PADX, pady=PADY)

        self.btn = tk.Button(
            self.root,
            text="Show messagebox",
            font=(FONT, FONT_SIZE_BIG),
            command=self.show_message,
        )
        self.btn.pack(padx=PADX, pady=PADY)

        self.btnclear = tk.Button(
            self.root, text="Clear", font=(FONT, FONT_SIZE_BIG), command=self.clear
        )
        self.btnclear.pack(padx=PADX, pady=PADY)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        state = self.checkbtn_state.get()
        if state == 0:
            print(self.tb.get("1.0", tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.tb.get("1.0", tk.END))

    def shortcut(self, event):
        # print(event.state, event.keysym, event)
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you want to exit?"):
            self.root.destroy()

    def clear(self):
        self.tb.delete("1.0", tk.END)


Program()
