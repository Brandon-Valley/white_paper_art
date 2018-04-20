import tkinter as tk
import GUI_utils

def demo(master):
    listbox = tk.Listbox(master)
#     listbox.pack(expand=1, fill="both")

    # inserting some items
    listbox.insert("end", "A list item")

    for item in ["one", "two", "three", "four"]:
        listbox.insert("end", item)

    # this changes the background colour of the 2nd item
    listbox.itemconfig(1, {'bg':'red'})

    # this changes the font color of the 4th item
    listbox.itemconfig(3, {'fg': 'blue'})

    # another way to pass the colour
    listbox.itemconfig(2, bg='green')
    
    color_tuple = (255,255,0)
    tk_rgb = "#%02x%02x%02x" % GUI_utils.round_color(color_tuple)
    
    
    listbox.itemconfig(2, bg=tk_rgb)
    listbox.itemconfig(0, foreground="purple")
    
    listbox.grid(column=1, row=1)


if __name__ == "__main__":
    root = tk.Tk()
    demo(root)
    root.mainloop()