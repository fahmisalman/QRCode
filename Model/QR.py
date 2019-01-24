import pyqrcode
import os


class QRCode(object):

    def __init__(self):
        self.filename = 'Output'
        self.link = ''
        self.qr = None
        pass

    def generate_qrcode(self):
        return pyqrcode.create(self.link)

    def save_png(self):
        self.qr.png('{}/Output/{}.png'.format(os.getcwd(), self.filename), scale=8)

    def save_svg(self):
        self.qr.svg('{}/Output/{}.svg'.format(os.getcwd(), self.filename), scale=8)

    def save_eps(self):
        self.qr.eps('{}/Output/{}.eps'.format(os.getcwd(), self.filename), scale=1)

    def fit(self, link, svg=False, eps=False, png=False, show=False):
        self.link = link
        self.qr = self.generate_qrcode()
        if png:
            self.save_png()
        if svg:
            self.save_svg()
        if eps:
            self.save_eps()
        if show:
            print(self.qr.terminal(quiet_zone=1))
