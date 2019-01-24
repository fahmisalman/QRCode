from Model import QRCode


if __name__ == '__main__':
    qr = QRCode()
    qr.fit('https://github.com/fahmisalman', svg=True, eps=True, show=True)
