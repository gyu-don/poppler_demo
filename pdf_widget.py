import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from popplerqt4 import Poppler

class Widget(QtGui.QLabel):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.doc = Poppler.Document.load(path)
        self.doc.setRenderHint(Poppler.Document.TextAntialiasing)
        self.n_pages = self.doc.numPages()
        self.current_page = 0
        self.load_current_page()

        next_page = QtGui.QAction('Next Page', self)
        next_page.setShortcut(QtCore.Qt.Key_Right)
        next_page.triggered.connect(self.next_page)
        self.addAction(next_page)

        prev_page = QtGui.QAction('Previous Page', self)
        prev_page.setShortcut(QtCore.Qt.Key_Left)
        prev_page.triggered.connect(self.prev_page)
        self.addAction(prev_page)

    def load_current_page(self):
        self.setPixmap(QtGui.QPixmap.fromImage(
                self.doc.page(self.current_page).renderToImage()))
        self.setWindowTitle('{0}/{1} - {2}'.format(
                self.current_page+1, self.n_pages, self.path))

    @QtCore.pyqtSlot()
    def next_page(self):
        self.current_page += 1
        if self.current_page >= self.n_pages:
            self.current_page = 0
        self.load_current_page()

    @QtCore.pyqtSlot()
    def prev_page(self):
        if self.current_page:
            self.current_page -= 1
        else:
            self.current_page = self.n_pages - 1
        self.load_current_page()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    file_path = QtGui.QFileDialog.getOpenFileName(
            None, 'Open PDF', '', 'PDF (*.pdf)')
    w = Widget(file_path)
    w.resize(600, 800)
    w.show()
    sys.exit(app.exec_())
