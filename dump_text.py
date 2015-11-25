import sys

from PyQt4 import QtCore
from popplerqt4 import Poppler

def dump_text(path):
    doc = Poppler.Document.load(path)
    for n,page in ((i+1, doc.page(i)) for i in range(doc.numPages())):
        print('\n-------- Page {0} -------'.format(n))
        for txtbox in page.textList():
            print(txtbox.text(), end=' ')

if __name__ == '__main__':
    app = QtCore.QCoreApplication(sys.argv)
    if len(sys.argv) != 2:
        print('Usage: {0} pdf_path'.format(sys.argv[0]))
    else:
        dump_text(sys.argv[1])
    sys.exit(0)
