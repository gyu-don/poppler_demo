#include <QApplication>
#include <QFileDialog>
#include "pdfwidget.h"

int main(int argc, char **argv)
{
	QApplication app(argc, argv);

	QString file_path = QString();
	
	while(file_path.isNull()){
		file_path = QFileDialog::getOpenFileName(
				0, "Open PDF", "", "PDF (*.pdf)");
	}

	PdfWidget w(file_path);
	w.resize(600, 800);
	w.show();
	return app.exec();
}
