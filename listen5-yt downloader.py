import tkinter as tk
window = tk.Tk()
window.title('yt downloader')
window.geometry('500x150')
window.resizable(False, False)
onlymusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = 'only music', variable = onlymusic, 
                       onvalue = True, offvalue = False)
check.pack()
window.mainloop()
