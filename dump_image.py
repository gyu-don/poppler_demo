import sys
import os.path
from contextlib import closing

from PyQt4 import QtCore
from popplerqt4 import Poppler

FORMAT = 'PNG'
EXT = '.png'

def dump_image(path):
    doc = Poppler.Document.load(path)
    doc.setRenderHint(Poppler.Document.TextAntialiasing)
    filename_fmt = os.path.splitext(path)[0] + '_{0}' + EXT
    for n,page in ((i+1, doc.page(i)) for i in range(doc.numPages())):
        f = QtCore.QFile(filename_fmt.format(n))
        with closing(f.open(QtCore.QIODevice.WriteOnly) and f):
            page.renderToImage().save(f, FORMAT)

if __name__ == '__main__':
    app = QtCore.QCoreApplication(sys.argv)
    if len(sys.argv) != 2:
        print('Usage: {0} pdf_path'.format(sys.argv[0]))
    else:
        dump_image(sys.argv[1])
    sys.exit(0)
