import tkinter as tk

class Example(tk.Frame):
    def __init__(self):

        tk.Frame.__init__(self)

        self.text_entry = tk.Entry(self, show = "*")
        self.text_entry.pack()
        self.btn1 = tk.Button(self, text="Toggle asterisk", command = self.toggle)
        self.btn1.pack()

    def toggle(self):
        if self.text_entry["show"] == "":
            self.text_entry["show"] = "*"

        else:
            self.text_entry["show"] = ""


if __name__ == "__main__":
    root=tk.Tk()
    Example().pack()
    root.mainloop()