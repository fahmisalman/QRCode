from Model import QRCode


if __name__ == '__main__':
    qr = QRCode()
    qr.fit('', png=True, svg=True, eps=True, show=True)
