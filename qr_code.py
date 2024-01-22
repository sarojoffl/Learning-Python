import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data("https://meta.wikimedia.org/wiki/User:Saroj")
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="white")
img.save("qr_code.png")
print("QR code generated and saved as qr_code.png")

