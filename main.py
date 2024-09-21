import yt_dlp

url = input("URL giriniz!: ")

yt_dlp.YoutubeDL({}).download([url])
