from pytube import YouTube
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
        print('目前進度: ' + str(progress) + '%')
yt = YouTube('https://www.youtube.com/watch?v=ZQTO9lxbBbc', on_progress_callback = showProgress)
stream = yt.streams.filter(res = '144p', fps = 30).first()

stream.download('youtube video', 'ghosghs kxxxxxxxxxxxxx battle area 144p 30fps')



