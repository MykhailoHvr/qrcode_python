from os import urandom
from unicodedata import name
import qrcode


def get_qrcode(url, name='default'):
    qr = qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR code create! name:{name}.png'


def main():
    url = input("input url:")
    name = input("input image name:")
    print(get_qrcode(url,name))


if __name__ == '__main__':
    main()