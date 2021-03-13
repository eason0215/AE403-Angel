import tkinter as tk
import tkinter.messagebox
def clickMe():
    tkinter.messagebox.showinfo(title = '提示', message = 'ouchhhhhhhhhhhhhhhhhhh!!!!!!!!!!!!!!')

window = tk.Tk()
window.title('幹什麼東西')
window.geometry('350x350')
label = tk.Label(window, text = 'gaegho0524 is poor LLLLLLLLLL', bg = '#000', fg = '#fff')
label.pack()

entry = tk.Entry(window, width = 20)
entry.pack()
button = tk.Button(window, text = 'fxxk', command = clickMe)
button.pack()
window.mainloop()


