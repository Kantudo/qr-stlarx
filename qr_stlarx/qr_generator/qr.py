import random
import string
from pathlib import Path
import os

STATIC = '/static/'

domain_url = 'https://qr.stlarx.com/'

QR_EXECUTABLE_NAME = 'qr'

STATIC_SHORTENED_QR = 'cachedqr/'
STATIC_SHORTENED_PDF = 'pdf_archive/'

INDEPENDENT_PATH = 'independent/'

QR_CACHE_DIRECTORY = INDEPENDENT_PATH + STATIC_SHORTENED_QR
PDF_ARCHIVE_DIRECTORY = INDEPENDENT_PATH + STATIC_SHORTENED_PDF

QR_EXT = '.png'

def new_id(directory=QR_CACHE_DIRECTORY):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    MON_PATH = os.path.join(BASE_DIR, directory)
    if not os.path.exists(MON_PATH):
        os.makedirs(MON_PATH)
    mon_id = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(11))
    for (root, dirnames, filename) in os.walk(MON_PATH):
        if mon_id in filename:
           mon_id = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(11))
    return mon_id

def createqr(str2encode):
    mon_id = new_id()
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    QR_PATH = os.path.join(BASE_DIR, QR_CACHE_DIRECTORY)
    filepath = QR_PATH + '/' + mon_id
    import subprocess
    
    subprocess.call([str(BASE_DIR.parent) + '/' + QR_EXECUTABLE_NAME, f'{filepath}',  f'{str2encode}'])

    return qr_id2static(mon_id, full_path=True)

def qr_id2static(mon_id, full_path=False):
    url = STATIC_SHORTENED_QR + mon_id + QR_EXT
    if full_path:
        url = STATIC + url
    return url

def pdf_id2static(mon_id, online_viewer=True):
    url = '/static/' + STATIC_SHORTENED_PDF + mon_id + '.pdf'

    if online_viewer:
        import urllib.parse
        url = 'viewer?file=' + urllib.parse.quote(url, safe='')

    return url

def write_pdf(f):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    pdf_id = new_id(directory=PDF_ARCHIVE_DIRECTORY)
    FILE_PATH= os.path.join(BASE_DIR, PDF_ARCHIVE_DIRECTORY + pdf_id + '.pdf')
    with open(FILE_PATH, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    mon_qr_path = createqr(domain_url + pdf_id2static(pdf_id))

    return mon_qr_path
