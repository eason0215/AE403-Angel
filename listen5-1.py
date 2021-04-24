import tkinter as tk
from pytube import YouTube
import threading

def onClick():
    global var
    var.set(entry.get())
    button.config(state = tk.DISABLED)
    label.config(text = 'downloading now...')
    try:
        yt = YouTube(var.get(), on_progress_callback = showProgress)
        if onlymusic.get():
            stream = yt.streams.filter(only_audio = True).first()
        else:
            stream = yt.streams.first()
        stream.download()
        button.config(state = tk.NORMAL)
        label.config(text = 'please type yt video 網址')
   
    except:
        print('download failed')
        button.config(state = tk.NORMAL)
        label.config(text = 'please type yt video 網址')
        
def thread():
    threading.Thread(target = thread).start()
    
progress = 0
def showProgress(stream, chunk, bytes_remaining):
    size = stream.filesize
    global progress
    
    preProgress = progress
    currentProgress = int((size - bytes_remaining) * 100 // size)
    progress = currentProgress
    if progress == 100:
        print('download complete!')
        
        return
    if preProgress != progress:
        scale.set(progress)
        window.update()
      
        print('目前進度: ' + str(progress) + '%')
window = tk.Tk()
window.title('yt video downloader')
window.geometry('500x150')
window.resizable(False, False)

    
    
label = tk.Label(window, text = 'please type yt video 網址')
label.pack()
var = tk.StringVar()
entry = tk.Entry(window, width = 50)
entry.pack()
onlymusic = tk.BooleanVar()
check = tk.Checkbutton(window, text = 'only music', variable = onlymusic, 
                       onvalue = True, offvalue = False)
check.pack()

button = tk.Button(window, text = 'download', command = onClick)
button.pack()
scale = tk.Scale(window, label = '進度條', orient = tk.HORIZONTAL, from_ = 0
                 , to = 100, length = 200, showvalue = False, tickinterval 
                 = 0)
scale.pack()
window.mainloop()