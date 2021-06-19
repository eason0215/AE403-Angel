import tkinter as tk
window = tk.Tk()
window.geometry('300x300')
for i in range(1, 10):
    for j in range(1, 10):
        l =tk.Label(window, text = i * j)
        l.grid(row = i, column = j, padx = 5, pady = 5)
window.mainloop()

