import tkinter as tk


try:                        # In order to be able to import tkinter for
    import tkinter as tk    # either in python 2 or in python 3
except:
    import Tkinter as tk


def swap():
    no_error_label.lift()
#     error_label.lift()
#     button2.lift()
    global is_button1_lifted
    if is_button1_lifted:
        button2.lift()
    else:
        button1.lift()
    is_button1_lifted = not is_button1_lifted


if __name__ == '__main__':
    root = tk.Tk()
    is_button1_lifted = False
    button1 = tk.Button(root, text="Swap with button 2", command=swap)
    button2 = tk.Button(root, text="Swap with button 1", command=swap)
    button3 = tk.Button(root, text="b3", command=swap)
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=3)
    
    
    

    
    
    error_label = tk.Label(root, text="error")
    no_error_label = tk.Label(root, text="no error")
    error_label.grid(row=1, column=1)
    no_error_label.grid(row=1, column=1)
    
    
    
    lift_error_button = tk.Button(root, text="lift error", command=error_label.lift)
    lower_error_button = tk.Button(root, text="lower error", command=no_error_label.lift)
    lift_error_button.grid(row=1, column=6)
    lower_error_button.grid(row=1, column=5)

    
    
    
    root.mainloop()