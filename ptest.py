# import tkinter as tk
# 
# class Demo1:
#     def __init__(self, master):
#         self.master = master
# #         self.frame = tk.Frame(self.master)
#         
#         self.text1 = StringVar()
#         self.test2 = StringVar()
#         
#         self.text1.trace("w", lambda name, index, mode, var=self.text1, self.update_tb2())
#         
#         
#         self.tb1 = tk.Entry(self.master,width=20)
#         self.tb2 = tk.Entry(self.master,width=20)
#         
#         
#         
#         self.tb1                .grid(column=1, row=2)
#         self.tb2                .grid(column=2, row=2)
#         
#         
#     def update_tb2(self):
#         self.tb2.insert(0, "siodhf")
#         
# #         s
# #         self.button1 = tk.Button(self.frame, text = 'New Window', width = 25, command = self.new_window)
# #         self.button1.pack()
# #         self.frame.pack()
# #     def new_window(self):
# #         self.newWindow = tk.Toplevel(self.master)
# #         self.app = Demo2(self.newWindow)
# # 
# # class Demo2:
# #     def __init__(self, master):
# #         self.master = master
# #         self.frame = tk.Frame(self.master)
# #         self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
# #         self.quitButton.pack()
# #         self.frame.pack()
# #     def close_windows(self):
# #         self.master.destroy()
# 
# def main(): 
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
# 
# if __name__ == '__main__':
#     main()