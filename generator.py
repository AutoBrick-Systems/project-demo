import qrcode

qr = qrcode.QRCode(
    version=1,  # controls size (1 = small, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high = more reliable scanning
    box_size=12,  # how big each square is
    border=4,  # white border (important!)
)

qr.add_data("https://autobrick-systems.github.io/project-demo/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")