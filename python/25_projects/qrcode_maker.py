import qrcode

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

img = qrcode.make(data)

img.save('C:/Users/anssi/Desktop/Testing/rick_roll.png')