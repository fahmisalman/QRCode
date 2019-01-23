import pyqrcode
import os


class QRCode(object):

    def __init__(self):
        self.filename = 'Output'
        self.link = ''
        self.qr = ''
        pass

    def generate_qrcode(self):
        return pyqrcode.create(self.link)

    def save_svg(self):
        self.qr.svg('{}/Output/{}.svg'.format(os.getcwd(), self.filename), scale=8)

    def save_eps(self):
        self.qr.eps('{}/Output/{}.eps'.format(os.getcwd(), self.filename), scale=8)

    def fit(self, link, svg=False, eps=False, show=False):
        self.link = link

        self.qr = self.generate_qrcode()
        if svg:
            self.save_svg()
        if eps:
            self.save_eps()
        if show:
            print(self.qr.terminal(quiet_zone=1))


if __name__ == '__main__':

    qrcode = QRCode()
    qrcode.fit('https://www.deezer.com/id/feed', show=True)