import qrcode
import qrcode.constants

def create(link):
    qr = qrcode.QRCode(
        version = None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size = 15,
        border = 4,
    )
    qr.add_data(link)
    qr.make(fit = True)

    image = qr.make_image(fill_color='black', back_color='white')
    return image



if __name__ == '__main__':
    name = input('Insert png name: ')
    link = input('Insert link: ')
    image = create(link)
    image.save(name + '.png')
