from Model import QRCode


if __name__ == '__main__':
    qr = QRCode()
    qr.fit('https://www.deezer.com/id/feed', svg=True, eps=True, show=True)
