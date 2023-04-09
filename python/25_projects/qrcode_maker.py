import qrcode

data = "REEEEEEEEEEEEE!"

img = qrcode.make(data)

img.save('C:/Users/anssi/Desktop/Testing/test.png')